import os
import unittest

from buzz import generator

def test_title():
    for x in range(0, generator.quotes_count(os.path.abspath('buzz/quotes'))):
        assert generator.generate_buzz(x).istitle()
