#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This class add a coloration to a node
"""

from __future__ import absolute_import
import os
import logging.handlers

PYTHON_LOGGER = logging.getLogger(__name__)
if not os.path.exists("log"):
    os.mkdir("log")
HDLR = logging.handlers.TimedRotatingFileHandler("log/coloration.log",
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


class Coloration:
    """
    This class add a coloration to a node
    """
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

    def __init__(self):
        """
        Constructor to init the coloration
        """
        self.coloration = {}

    def color_node(self, node, color):
        """
        Add coloration to a input node
        :param node: (string) Node name to add a coloration
        :param color: (string) coloration name. You can use this 3 constants
                    Coloration.RED, Coloration.GREEN, Coloration.BLUE
        :return: (bool) True coloration is add False the input node have already a coloration
        """
        if node not in self.coloration:
            self.coloration[node] = color
            return True
        else:
            return False


if __name__ == "__main__":
    pass