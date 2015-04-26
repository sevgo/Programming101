#!/usr/bin/env python3

from unittest import main, TestCase
from github_crowler import github_auth


class Test_GitHUB_Crowller(TestCase):
    def setUp(self):
        self.credentials = github_auth("cred.json")

    def test_credentials(self):
        self.assertIsInstance(self.credentials, dict)

if __name__ == "__main__":
    main()
