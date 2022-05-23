'''Async fetcher for parsing html'''
from argparse import ArgumentParser
import re
import time
import asyncio
import aiohttp
import aiofiles

from counter import Counter


async def fetcher(result, session, urls_queue, counter):
    '''Fetcher implementation'''
    while True:
        url = await urls_queue.get()

        try:
            async with session.get(url) as resp:
                print(url)
                data = await resp.read()
                tokens = re.findall(r'[a-zа-я]+', data.lower().decode('utf-8'))
                result[url] = counter.get_top_k(url, tokens)
        except aiohttp.client_exceptions.InvalidURL:
            result[url] = {}
        finally:
            urls_queue.task_done()


async def add_url_in_queue(urls_queue, urls_path):
    '''Add url in queue'''
    async with aiofiles.open(urls_path, 'r') as fin:
        async for line in fin:
            await urls_queue.put(line.strip())


async def crawl(result, urls_path='urls.txt', max_queue_size=30, n_threads=10):
    '''Crawl'''
    counter = Counter(top_k=5, ignore_words="ignore_words.txt")
    urls_queue = asyncio.Queue(maxsize=max_queue_size)

    read_task = asyncio.create_task(add_url_in_queue(urls_queue, urls_path))
    await asyncio.sleep(1)

    async with aiohttp.ClientSession() as session:

        tasks = [
            asyncio.create_task(fetcher(result, session, urls_queue, counter))
            for _ in range(n_threads)
        ]

        await urls_queue.join()

    print(f'Size : {urls_queue.qsize()}')
    read_task.cancel()
    for task in tasks:
        task.cancel()

parser = ArgumentParser()
parser.add_argument('-c', type=int, nargs='?')
parser.add_argument('ints', type=int, nargs='?')
parser.add_argument('strs', type=str)


async def main(n_threads=10, urls_path='urls.txt'):
    '''Main'''
    t_1 = time.perf_counter()

    res = {}
    await crawl(
            res,
            urls_path=urls_path,
            max_queue_size=70,
            n_threads=n_threads,
        )

    print(res, len(res.keys()))
    t_2 = time.perf_counter()
    print(f"Time = {t_2 - t_1}")


if __name__ == '__main__':
    args = parser.parse_args()
    n_threads_arg = vars(args)['c'] or vars(args)['ints']
    urls_path_arg = vars(args)['strs']

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main(n_threads_arg, urls_path_arg))
