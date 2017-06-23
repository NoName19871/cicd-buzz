# -*- coding: utf-8 -*-
import os
import random

def path_to_quotes():
	path = os.getcwd()
	if (path.endswith('cicd-buzz')):
		path = 'buzz/quotes'
	elif (path.find('cicd-buzz') == -1):
		path = 'src/buzz/quotes'
	else:
		path = '../buzz/quotes'
	return path

def quotes_count():
	return sum(1 for i in open(path_to_quotes(), 'r'))

def generate_buzz(n):
	f = open(path_to_quotes(), 'r')
	tmp = 0
	for line in f:
		if (tmp == n):
			return line[0:line.find('|')].title()
		else:
			tmp = tmp + 1

if __name__ == "__main__":
    print(generate_buzz(random.randrange(0, quotes_count())))
