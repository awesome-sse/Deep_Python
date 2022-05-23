'''Testing fetcher'''
import asyncio
import os
import unittest
from unittest.mock import MagicMock

import aiohttp
from aiohttp.test_utils import AioHTTPTestCase

import fetcher
from counter import Counter


class TestCounter(unittest.TestCase):
    '''Test Counter'''
    def test_add(self):
        '''Test add for counter'''
        counter = Counter()
        self.assertEqual(counter.data, {})
        counter.add("1")
        counter.add("2")
        counter.add("3")
        counter.add("1")
        self.assertEqual(counter.data, {"1": 2, "2": 1, "3": 1})

    def test_extend(self):
        '''Test extend for counter'''
        url = "url.com"
        elems = [f"{i}" for i in range(3)]
        counter = Counter()
        self.assertEqual(counter.cache, {})
        counter.extend(url, elems)

        self.assertEqual(counter.cache, {"url.com": {"0": 1, "1": 1, "2": 1}})
        self.assertEqual(counter.data, {})

    def test_reset(self):
        '''Test reset for counter'''
        counter = Counter()
        self.assertEqual(counter.data, {})
        counter.add("1")
        counter.add("2")
        counter.add("3")
        counter.add("1")
        counter.reset()
        self.assertEqual(counter.data, {})

    def test_get_top_k(self):
        '''Test top k for counter'''
        url = "url.com"
        elems = [f"{i}" for i in range(9)]
        elems += [f"{i}" for i in range(3)]
        elems += [f"{i}" for i in range(2)]
        elems += [f"{i}" for i in range(1)]
        counter = Counter(top_k=3)
        top = counter.get_top_k(url, elems)
        self.assertEqual(top, {"0": 4, "1": 3, "2": 2})


class MockSessionResp:
    '''For aiohttp.get()'''
    async def __aenter__(self):
        return self

    async def __aexit__(self, *args, **kwargs):
        await asyncio.sleep(0)

    async def read(self):
        '''Mock for resp.read()'''
        html_test = b"Hello, I am html text! Bye, bye"
        return html_test


class FetcherTest(AioHTTPTestCase):
    '''Test fetcher'''
    def setUp(self):
        self.urls_test = [
            "https://www.lamoda.ru/p/mp002xrr/clothes-gloriajeans-futbolka/\n",
            "https://www.lamoda.ru/p/rtl65301/clothes-hugo-futbolka/\n",
            "https://www.lamoda.ru/p/mp002x9u/clothes-tomtailor-futbolka/\n",
            "https://www.lamoda.ru/p/mpm08crr/clothes-gloriajeans-futbolka/\n",
            "https://www.lamoda.ru/p/rtla5301/clothes-hugo-futbolka/\n",
        ]
        self.urls = 'urls_test.txt'
        with open(self.urls, 'w', encoding='utf-8') as fout:
            fout.writelines(self.urls_test)

    def tearDown(self):
        os.remove(self.urls)

    async def test_fetcher(self):
        '''Test fetcher async'''
        test_q = asyncio.Queue()
        await test_q.put("url.com")

        async with aiohttp.ClientSession() as session:
            session.get = MagicMock(return_value=MockSessionResp())

            result = {}
            counter_cache = Counter(top_k=10)
            task = asyncio.create_task(fetcher.fetcher(
                result,
                session,
                test_q,
                counter_cache
            ))

            await test_q.join()
            task.cancel()

        expected = {"url.com": {'bye': 2, 'hello': 1, 'i': 1,
                    'am': 1, 'html': 1, 'text': 1}}

        self.assertDictEqual(result, expected)

    async def test_add_url_in_queue(self):
        '''Test add elem in queue'''
        test_q = asyncio.Queue()

        await fetcher.add_url_in_queue(test_q, self.urls)

        urls_result = []
        while not test_q.empty():
            urls_result.append(await test_q.get())

        self.assertEqual(len(urls_result), len(self.urls_test))
        self.assertEqual(
            urls_result,
            list(map(lambda url: url.strip(), self.urls_test))
        )


if __name__ == '__main__':
    unittest.main()
