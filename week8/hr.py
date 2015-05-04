#!/usr/bin/env python3

import requests as req
import json


class HackBulgaria:

    @staticmethod
    def read_json_from_web(url):
        r = req.get(url)
        json_data = r.json()

        return HackBulgaria(json_data)

    JSON_FILE = 'students.json'

    def __init__(self, json_data):
        self.data = json_data

    def print_json(self):
        for el in self.data:
            print(el)


if __name__ == "__main__":
    hb = HackBulgaria.read_json_from_web(
        'https://hackbulgaria.com/api/students/')

    hb.print_json()
