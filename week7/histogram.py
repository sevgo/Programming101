#!/usr/bin/env python3
import matplotlib.pyplot as plt

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

    def draw(self):
        servers = []
        counts = []
        for key, value in self.items():
            servers.append(key)
            counts.append(value)

        x = servers
        y = counts

        width = list(range(len(x)))

        plt.bar(width, y, align="center")
        plt.xticks(width, x)
        plt.xlabel("Server")
        plt.ylabel("Count")
        plt.title(".bg servers")
        plt.save("servers_in_bgweb.png")
