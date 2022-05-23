'''Server for parsing websites'''
import argparse
import socket
from queue import Queue
import threading
from urllib.request import urlopen
from urllib.error import HTTPError
import re
import json

from counter import Counter


class Server():
    '''Server implementation'''
    def __init__(self, num_workers=10, num_top=5):
        self.n_workers = num_workers
        self.workers = []

        self.n_top = num_top

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.clients = set()
        self.clients_to_remove = set()
        self.tasks_queue = Queue()

        self.total_urls = 0

        self.tick_rate = 1
        self.sock.settimeout(self.tick_rate)

        self.th_lock = threading.Lock()

    def _accept_connection(self):
        try:
            client, addr = self.sock.accept()
        except socket.timeout:
            return
        else:
            print('New connection:', addr)
            self.clients.add(client)

    def _recv_from_client(self, client):
        try:
            data = client.recv(4096)
        except socket.timeout:
            return
        else:
            if data != b'':
                print('Data from client:', data)
                self.tasks_queue.put((data, client))
            else:
                self.clients_to_remove.add(client)

    def _print_n_clients(self):
        print('Number of clients:', len(self.clients))

    def _print_statistic(self):
        self.th_lock.acquire()
        self.total_urls += 1
        print(f'Number of processed urls = {self.total_urls} ')
        self.th_lock.release()

    def worker(self, k):
        '''Worker'''
        counter = Counter(top_k=k, ignore_words="ignore_words.txt")
        while True:
            if not self.tasks_queue.empty():
                url, client = self.tasks_queue.get()
                try:
                    url_file = urlopen(url.decode("utf-8"))
                except HTTPError:
                    client.send(b'{}')
                else:
                    text = url_file.read().decode("utf-8")
                    text = re.findall(r'[a-zа-я]+', text.lower())

                    client.send(json.dumps(
                            counter.get_top_k(url, text)
                        ).encode("utf-8")
                    )
                    self._print_statistic()

    def event_loop(self):
        '''Master'''
        self.sock.bind(('', 15000))
        self.sock.listen(1000)

        for i in range(self.n_workers):
            self.workers.append(
                threading.Thread(
                    target=self.worker,
                    args=(self.n_top,)
                )
            )
            self.workers[i].start()

        while True:

            self._accept_connection()
            self._print_n_clients()

            for i, client in enumerate(self.clients):
                self._recv_from_client(client)

            for client_to_remove in self.clients_to_remove:
                self.clients.remove(client_to_remove)

            self.clients_to_remove.clear()

        for worker in self.num_workers:
            worker.join()


parser = argparse.ArgumentParser()
parser.add_argument("-w", dest="num_workers", type=int,
                    required=True,
                    )

parser.add_argument("-k", dest="num_top", type=int,
                    required=True,
                    )


if __name__ == "__main__":
    args = parser.parse_args()
    server = Server(**vars(args))
    server.event_loop()
