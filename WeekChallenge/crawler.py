#!/usr/bin/env python3
import requests as req
from bs4 import BeautifulSoup as bs

class Crawler:

    def __init__(self, url):
        self.url = url
        self.internal_links = []
        self.external_links = []
        self.visited = []

    def start(self):
       links = self.get_links_from_url(self.url)
       self.classify(links)
       self.visited.append(self.url)

       for link in self.internal_links:
           if link not in self.visited:
               print(link)
               self.visited.append(link)
               sub_pages = self.get_links_from_url(link)
               self.classify(sub_pages)


    def get_links_from_url(self, url):
        try:
            links =  set()
            r = req.get(url, timeout=2)
            soup = bs(r.text)

            for link in soup.find_all('a'):
                links.add(link.get('href'))

        except Exception as err:
            print("Error ocurred: {}".format(err))

        return links


    def classify(self, links):

        for link in links:
            if link is None:
                continue

            if 'start.bg' in link:
                self.internal_links.append(link)
            elif 'link.php' in link:
                self.external_links.append(link)

        # return external


def main():
    crawler = Crawler('http://www.start.bg')
    # links = crawler.get_links_from_url('http://www.start.bg')
    # print(crawler.classify(links))
    crawler.start()

if __name__ == "__main__":
    main()
