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
        if link.startswith("link"):
            link = self.url + '/' + link

        return link

    def create_url_list(self):
        links = []
        page = _req.get(self.url)
        soup = BeautifulSoup(page.text)
        for link in soup.find_all('a'):
            address = link.get('href')
            if address and address[0] != '#' and address[0] != '/':
                address = self._normalize_url(address)
                links.append(address)

        return links

    def real_links(self, links_list):
        pass

if __name__ == "__main__":
    c = Crowler("http://register.start.bg")
    c.create_url_list()
    for element in c.links:
        print("---------------------------------")
        print(element)
