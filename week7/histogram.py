#!/usr/bin/env python3


class Histogram:
    def __init__(self):
        self.histogram = {}

    def add(self, agent):
        if agent in self.histogram:
            self.histogram[agent] += 1
        else:
            self.histogram[agent] = 1

    def count(self, agent):
        return self.histogram[agent]

    def get_dict(self):
        return self.histogram

    # Function for testing purposes
    def _have_agent(self, agent):
        if agent in self.histogram:
            return True

        return False

    def items(self):
        return self.histogram.items()
