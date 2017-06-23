import os
import random

def quotes_count(filename):
	return sum(1 for i in open(filename, 'r'))

def generate_buzz(n):
	f = open(os.path.abspath('buzz/quotes'), 'r')
	tmp = 0
	for line in f:
		if (tmp == n):
			return line[0:line.find('|')].title()
		else:
			tmp = tmp + 1

if __name__ == "__main__":
    print(generate_buzz(random.randrange(0, quotes_count(os.path.abspath('buzz/quotes')))))
