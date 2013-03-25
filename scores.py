#!/usr/bin/python

from sys import argv
from xml.etree import ElementTree

'''
Utility to output a sorted list of raw scores from an FRC Spy XML file
Copyright 2013 Thomas Clark
'''
def main():
	matches = ElementTree.parse(argv[1]).getroot()
	scores = []
	
	for match in matches:
		if match.findtext('typ') != 'P':
			scores += [int(match.findtext('r' + argv[2]))]
			scores += [int(match.findtext('b' + argv[2]))]
		
	print('\n'.join(map(str, (sorted(scores)))))

if __name__ == '__main__':
	main()

