#!/usr/bin/env python3
from graf import Graph
import requests as _req
import json


def github_auth(path):
    with open(path, 'r') as fd:
        cred = json.load(fd)

    return dict(cred)

def github_request(credentials, user):
    _url = credentials['url']
    _id = credentials['client_id']
    _secret = credentials['client_secret']
    github_user = _url + user
    github_token = '?client_id=' + _id + '&client_secret=' + _secret
    github_request = github_user + github_token
    print(github_request)
    return _req.get(github_request)


if __name__ == "__main__":
    print(github_request(github_auth('cred.json'), 'sevgo'))
