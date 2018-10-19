#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A file with a graph class
"""

from __future__ import absolute_import
import os
import timeit
import logging.handlers

PYTHON_LOGGER = logging.getLogger(__name__)
if not os.path.exists("log"):
    os.mkdir("log")
HDLR = logging.handlers.TimedRotatingFileHandler("log/Graphe.log",
                                                 when="midnight", backupCount=60)
STREAM_HDLR = logging.StreamHandler()
FORMATTER = logging.Formatter("%(asctime)s %(filename)s [%(levelname)s] %(message)s")
HDLR.setFormatter(FORMATTER)
STREAM_HDLR.setFormatter(FORMATTER)
PYTHON_LOGGER.addHandler(HDLR)
PYTHON_LOGGER.addHandler(STREAM_HDLR)
PYTHON_LOGGER.setLevel(logging.DEBUG)

# Absolute path to the folder location of this python file
FOLDER_ABSOLUTE_PATH = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))


class Graph:
    """
    Class graph to represent a graph
    """

    def __init__(self):
        """
        Constructor to create a graph with nothing inside
        """

        self.graph = {}

    def add_node(self, node_name, links):
        """
        Function to add a node to the graph
        :param node_name: (string) Key name of the node
        :param links: (list of string) All the nodes linked to the created node
        """

        if node_name not in self.graph:
            self.graph[node_name] = links
        else:
            self.graph[node_name].extend(links)
        for node in links:
            if node not in self.graph:
                self.graph[node] = [node_name]
            else:
                self.graph[node].append(node_name)

    def get_nodes(self):
        """
        Function to get all nodes of the graph
        :return: (list) All the graph's nodes
        """

        return list(self.graph.keys())

    def display_graph(self):
        """
        Function to isplay the graph in the terminal
        """

        PYTHON_LOGGER.info(self.graph)


if __name__ == "__main__":
    g = Graph()
    g.add_node("S1", ["S2", "S3", "S4"])
    g.display_graph()
    g.add_node("S4", ["S5"])
    g.display_graph()
