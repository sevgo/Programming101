#!/usr/bin/env python3

from histogram import Histogram
import requests as _req
from bs4 import BeautifulSoup


class Crowler:

    def __init__(self, url):
        self.url = url
        self.histogram = Histogram()
        self.links = []

    def _normalize_url(self, link):
        return self.url + '/' + link

    def _raw_links(self):
        tmp_links = []
        page = _req.get(self.url)
        soup = BeautifulSoup(page.text)
        for link in soup.find_all('a'):
            url = link.get('href')
            if url is not None:
                if url.startswith('h'):
                    tmp_links.append(url)
                elif url.startswith('l'):
                    tmp_links.append(self._normalize_url(url))
                else:
                    continue

        return tmp_links

    def real_links(self):
        links = self._raw_links()
        for element in links:
            try:
                r = _req.head(element, allow_redirects=True, timeout=10)
                print(r.url)
                self.links.append(r.url)
            except TimeOut as err:
                print("TimeOut: {}".format(err))

        return True

if __name__ == "__main__":
    c = Crowler("http://register.start.bg")
    c.real_links()
    for element in c.links:
        print(element)
