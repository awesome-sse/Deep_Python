'''Testing server and client'''
import json
import socket
import unittest
from unittest.mock import MagicMock, patch
from queue import Queue
from client import split_for_threads

import client
import server
from counter import Counter


class TestCounter(unittest.TestCase):
    '''Test counter'''
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


class TestClient(unittest.TestCase):
    '''Test client'''
    def setUp(self):

        self.top_k_test = {"1": 5, "2": 4, "3": 3}

        self.response_test = json.dumps(self.top_k_test).encode("utf-8")

    def test_split(self):
        '''Test split for client'''
        urls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(split_for_threads(urls, 3),
                         [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]])

    def test_client_worker(self):
        '''Test client worker'''
        with patch.multiple(socket.socket,
                            connect=MagicMock(return_value=None),
                            send=MagicMock(return_value=None),
                            recv=MagicMock(return_value=self.response_test),
                            ) as _:
            test_q = Queue()
            test_urls = ["1"] * 3
            client.client_worker(test_q, test_urls)

        while not test_q.empty():
            resp = test_q.get()
            self.assertEqual(resp, self.top_k_test)


class TestServer(unittest.TestCase):
    '''Test server'''
    def test_accept_connection(self):
        '''Test server accept connection'''
        with patch.multiple(socket.socket,
                            accept=MagicMock(return_value=(1, "localhost")),
                            ) as _:
            test_server = server.Server()
            test_server._accept_connection()
            self.assertEqual(test_server.clients, set([1]))
            test_server.sock.close()

    def test_recv_from_client(self):
        '''Test server receive data'''
        with patch.multiple(socket.socket,
                            recv=MagicMock(return_value="url.com"),
                            ) as _:
            test_server = server.Server()
            test_server._recv_from_client(socket.socket)

            self.assertEqual(test_server.tasks_queue.get(),
                             ("url.com", socket.socket))
            test_server.sock.close()


if __name__ == '__main__':
    unittest.main()
