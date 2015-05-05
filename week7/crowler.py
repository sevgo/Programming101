#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from histogram import Histogram
import requests as _req
from urllib.parse import urlsplit
from bs4 import BeautifulSoup


class Crowler:

    MY_DOMAIN = '.bg'
    HEADER = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0"
        }

    def __init__(self, url):
        self.url = url
        self.histogram = Histogram()
        self.links = []

    def _normalize_url(self, link):
        return self.url + '/' + link

    def is_BG(self, link):
        return link[len(link) - len(Crowler.MY_DOMAIN):] == Crowler.MY_DOMAIN

    def _raw_links(self):
        tmp_links = []
        page = _req.get(self.url, headers=Crowler.HEADER)
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

    def server(self, srv):
        servers = ['apache', 'nginx', 'iis', 'lighttpd']
        for element in servers:
            if element in srv.lower():
                return element

        return 'other'

    def real_links(self):
        links = self._raw_links()
        visited = set()
        for element in links:
            try:
                r = _req.head(element, allow_redirects=True, timeout=3,
                              headers=Crowler.HEADER)
                u = urlsplit(r.url)
                if u.netloc not in visited and self.is_BG(u.netloc):
                    self.links.append(u.scheme + "://" + u.netloc)
                    web_srv = self.server(r.headers['server'])
                    self.histogram.add(web_srv)
                    visited.add(u.netloc)

            except Exception as err:
                print("Error: {} occured...".format(err))

        if 0 == len(self.links):
            return False

        return True

if __name__ == "__main__":
    c = Crowler("http://register.start.bg")
    if c.real_links():
        c.histogram.draw()
