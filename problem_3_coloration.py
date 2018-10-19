#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main file with every problems
"""

from __future__ import absolute_import
from graph import Graph
from coloration import Coloration
import os
import timeit
import logging.handlers

PYTHON_LOGGER = logging.getLogger(__name__)
if not os.path.exists("log"):
    os.mkdir("log")
HDLR = logging.handlers.TimedRotatingFileHandler("log/problem_3_coloration.log",
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


def check_certificate(graph_to_test, coloration_to_test):
    """
    Function to check a coloration is a valid 3-coloration for his graph
    :param graph_to_test: (Graph) The graph we want to test
    :param coloration_to_test: (Coloration) The graph's coloration
    :return: (boolean) True if the 3-coloration is valid, False if it is not
    """

    for node in graph_to_test.graph:
        for link in graph_to_test.graph[node]:
            if coloration_to_test.coloration[node] == coloration_to_test.coloration[link]:
                return False
    return True


if __name__ == "__main__":
    my_graph = Graph("sample_graph.txt")
    nodes = my_graph.get_nodes()

    my_coloration = Coloration()
    my_coloration.color_node("s1", Coloration.BLUE)
    my_coloration.color_node("s2", Coloration.GREEN)
    my_coloration.color_node("s3", Coloration.RED)
    my_coloration.color_node("s4", Coloration.RED)

    my_graph.display_graph(my_coloration)

    PYTHON_LOGGER.info(check_certificate(my_graph, my_coloration))