"""Testting parse_html function and callbacks"""
import unittest
from random import randint
from unittest import TestCase
from unittest.mock import patch
from faker import Faker

import parse_html


class TestParseHTML(TestCase):
    """Testing parse_html and functions"""

    def test_open_tag_func(self):
        """Testing open_tags_func"""
        parse_html.TAGS_COUNT = {}
        parse_html.open_tag_func('html')
        parse_html.open_tag_func('p')
        tags_count = parse_html.open_tag_func('p')
        self.assertEqual(tags_count, {'html': 1, 'p': 2})

    def test_data_func(self):
        """Testing data_func with Faker"""
        fake = Faker()
        len_text = 0
        parse_html.DATA_LEN = 0
        html = []
        for _ in range(10):
            text = fake.text(100)
            len_text += len(text)
            html.append(text)

        for text in html:
            parse_html.data_func(text)

        self.assertEqual(parse_html.DATA_LEN, len_text)

    def test_close_tag_func(self):
        """Testing close_tags_func"""
        parse_html.TAGS_COUNT = {}
        parse_html.DATA_LEN = 0
        parse_html.open_tag_func('html')
        parse_html.open_tag_func('p')
        parse_html.open_tag_func('p')
        self.assertEqual(parse_html.close_tag_func(), 'p')

    @patch('parse_html.open_tag_func', return_value=None)
    @patch('parse_html.data_func', return_value=None)
    @patch('parse_html.close_tag_func', return_value=None)
    def test_parse_html(self, open_tag_mock, data_mock, close_tag_mock):
        """ Testing parse_html using mocks and Faker """

        n_call = randint(1, 20)
        html = parse_html.generate_html(n_call)

        parse_html.parse_html(html, open_tag_mock, data_mock, close_tag_mock)

        self.assertEqual(open_tag_mock.call_count, n_call)
        self.assertEqual(data_mock.call_count, n_call * 2)
        self.assertEqual(close_tag_mock.call_count, n_call)


if __name__ == "__main__":
    unittest.main()
