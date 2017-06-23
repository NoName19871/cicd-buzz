import os
import unittest

from buzz import generator

def test_title():
    for x in range(1, generator.quotes_count(os.path.abspath('buzz/quotes')) - 2):
        assert generator.generate_buzz(x).istitle()
