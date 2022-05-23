'''
    Counter cache - using to find
    most popular tokens in list of tokens
'''
from itertools import islice
import re

class Counter:
    '''Counter implimentation'''
    def __init__(self, top_k=5, ignore_words = None):
        self.data = {}
        self.cache = {}
        self.top_k = top_k
        self.ignore = set()

        if ignore_words:
            with open(ignore_words, 'r', encoding='utf-8') as fin:
                for line in fin.readlines():
                    for elem in re.findall(r'[a-zа-я]+', line):
                        self.ignore.add(elem)

    def add(self, elem):
        '''Add one token to data'''
        if elem not in self.ignore:
            if elem in self.data:
                self.data[elem] += 1
            else:
                self.data[elem] = 1

    def extend(self, url, elems: list):
        '''Add tokens to data'''
        for elem in elems:
            self.add(elem)
        self.cache[url] = dict(islice(dict(sorted(self.data.items(), key=lambda item: item[1], reverse=True)).items(), self.top_k))
        self.reset()

    def reset(self):
        '''Reset data'''
        self.data = {}

    def get_top_k(self, url, data):
        '''Getting most popular tokens'''
        if url not in self.cache:
            self.extend(url, data)
        return self.cache[url]
