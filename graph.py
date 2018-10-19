#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A file with a graph class
"""

from __future__ import absolute_import
import os
import matplotlib.pyplot as plt
import networkx as nx
import logging.handlers
from coloration import Coloration

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
        Add a node to the graph
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

    def display_graph(self, coloration):
        """
        Display the graph in the terminal
        :param coloration: (coloration) coloration for each node
        """
        graph_nx = nx.Graph()
        labels = {}
        node_color = []
        for node in self.graph:
            for neighbour in self.graph[node]:
                graph_nx.add_edge(node, neighbour)
            labels[node] = node
            node_color.append(coloration.coloration[node])
        nx.draw(graph_nx, node_color=node_color, labels=labels)
        plt.axis('off')
        plt.show()


if __name__ == "__main__":
    g = Graph()
    coloration = Coloration()
    g.add_node("S1", ["S2", "S3", "S4"])
    g.add_node("S3", ["S2"])
    coloration.color_node("S1", coloration.BLUE)
    coloration.color_node("S2", coloration.RED)
    coloration.color_node("S3", coloration.GREEN)
    coloration.color_node("S4", coloration.GREEN)
    g.display_graph(coloration)
