"""Parse html with callback"""
from random import randint
from faker import Faker


TAGS_NAMES = ['html', 'td', 'h1', 'h2', 'h3', 'h4', 'h5',
              'h6', 'script', 'style', 'hr', 'title', 'div', 'link', 'p']
TAGS_COUNT = {}
DATA_LEN = 0
MOST_FREQ_TAG = ""


def open_tag_func(tag):
    """Callback for open tag"""

    if tag in TAGS_COUNT:
        TAGS_COUNT[tag] += 1
    else:
        TAGS_COUNT[tag] = 1

    return TAGS_COUNT


def data_func(data):
    """Callback for data inside tag"""
    global DATA_LEN

    DATA_LEN += len(data)
    return DATA_LEN


def close_tag_func():
    """Callback for close tag"""
    global MOST_FREQ_TAG

    MOST_FREQ_TAG = ""
    for tag, cnt in TAGS_COUNT.items():
        if MOST_FREQ_TAG == "" or cnt >= TAGS_COUNT[MOST_FREQ_TAG]:
            MOST_FREQ_TAG = tag

    return MOST_FREQ_TAG


def generate_html(tag_count=1):
    """Generate html with tags"""
    fake = Faker()

    def add_tag_with_text(tag_count, tag_cnt=0):
        text = ""

        if not tag_count <= tag_cnt:
            tag = TAGS_NAMES[randint(0, len(TAGS_NAMES) - 1)]

            text += "<" + tag + ">"
            text += fake.text(10)
            text += add_tag_with_text(tag_count, tag_cnt + 1)
            text += fake.text(10)
            text += "</" + tag + ">"

        return text

    return add_tag_with_text(tag_count, 0)


def parse_html(html_str: str, open_tag_callback,
               data_callback, close_tag_callback):
    """Parse html-string with callback"""
    temp_str = ""
    close_tag = False

    for char in html_str:
        if char == "<":
            close_tag = False
            data_callback(temp_str)
            temp_str = ""

        elif char == "/":
            close_tag = True

        elif char == ">":
            if close_tag:
                close_tag_callback()
            else:
                open_tag_callback(temp_str)

            temp_str = ""

        else:
            temp_str += char


if __name__ == "__main__":
    html = generate_html(5)

    parse_html(html, open_tag_func, data_func, close_tag_func)

    print("HTML:\n", html, sep="")
    print("Tags count:", TAGS_COUNT)
    print("Data length:", DATA_LEN)
    print("Most frequence tag:", MOST_FREQ_TAG)
