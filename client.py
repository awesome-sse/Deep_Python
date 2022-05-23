'''Client for server requests'''
import argparse
from queue import Queue
import threading
import socket
import json
from math import floor


def split_for_threads(urls, n_threads):
    '''Split urls for transmission to the thread'''
    n_fold = floor(len(urls) / n_threads)
    split_urls = []
    for i in range(n_threads - 1):
        split_urls.append(urls[i * n_fold: i * n_fold + n_fold])
    split_urls.append(urls[(n_threads - 1) * n_fold:])
    return split_urls


def client_worker(client_q, urls: list):
    '''Client worker'''
    sock = socket.socket()
    sock.connect(('127.0.0.1', 15000))

    for url in urls:
        sock.send(url.encode("utf-8"))
        data = json.loads(sock.recv(1024).decode("utf-8"))
        client_q.put(data)
        print(data)

    sock.close()


def main(n_threads, urls_file):
    '''Read txt file and activate threads for requests on server'''

    with open(urls_file, 'r', encoding="utf-8") as fin:
        urls = [line.strip() for line in fin.readlines()]

    client_q = Queue()
    threads = []

    split_urls = split_for_threads(urls, n_threads)
    for i, batch_urls in enumerate(split_urls):
        threads.append(
            threading.Thread(
                target=client_worker,
                args=(client_q, batch_urls,)
            )
        )
        threads[i].start()

    for worker in threads:
        worker.join()

    print(f'JSON Received: {client_q.qsize()}')


parser = argparse.ArgumentParser()
parser.add_argument('ints', metavar='N', type=int, nargs='+')
parser.add_argument('strs', metavar='N', type=str, nargs='+')


if __name__ == '__main__':
    args = parser.parse_args()
    n = vars(args)['ints'][0]
    urls_path = vars(args)['strs'][0]
    main(n, urls_path)
