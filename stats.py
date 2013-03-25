#!/usr/bin/python

import numpy

'''
Prints some additional information about the distribution of scores.
Copyright 2013 Thomas Clark
'''

# Final finscores
finscores = [float(score) for score in filter(lambda score: score.isdigit(), open('finscores.dat').read().split('\n'))]

# Foul points
fscores = [float(score) for score in filter(lambda score: score.isdigit(), open('fptsscores.dat').read().split('\n'))]

# Bridge (pyramid?) finscores
bscores = [float(score) for score in filter(lambda score: score.isdigit(), open('bptsscores.dat').read().split('\n'))]

def main():
	print 'Pyramid socres:'
	for score in (0, 10, 20, 30, 40, 50, 60, 70 , 80, 90):
		print '\t', score, '\t', round(float(bscores.count(score)) / len(bscores) * 100, 3), '%'
	
	print 'Final scores:'
	print '\tmean:\t\t\t', numpy.mean(finscores)
	print '\tstddev:\t\t\t', numpy.std(finscores)
	print '\tfrequency of 0s:\t', len(filter(lambda x: x == 0, finscores)) / float(len(finscores)) * 100, '%'
	print '\t10th percentile\t\t', finscores[len(finscores) * 1/10 - 1]
	print '\t25th percentile\t\t', finscores[len(finscores) * 1/4 - 1]
	print '\tmedian:\t\t\t', finscores[len(finscores) / 2]
	print '\t75th percentile\t\t', finscores[len(finscores) * 3/4 - 1]
	print '\t90th percentile\t\t', finscores[len(finscores) * 9/10 - 1]
	print '\thighest score:\t\t', max(finscores)
	
	print round(100 * sum(bscores) / sum(finscores), 1), '% of points were from pyramids'
	print round(100 * sum(fscores) / sum(finscores), 1), '% of points were from fouls'
	print round(100 * (sum(finscores) - sum(bscores) - sum(fscores)) / sum(finscores), 1), '% of points were from discs'
	print 'The top 10% scored {}% of the points'.format(round(100 * sum(finscores[int(len(finscores) * 0.9 - 1):]) / sum(finscores), 1))
	print '{}% of alliances had penalties'.format(round(100 - 100 * fscores.count(0) / len(fscores)))
	print 'There were {} total penalty points'.format(sum(fscores))
	print '{}% of scores were 0'.format(100.0 * finscores.count(0) / len(finscores))

if __name__ == '__main__': main()

