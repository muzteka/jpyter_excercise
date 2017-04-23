# -*- coding: UTF-8 -*-

import csv


def import_csv(file):
	csvfile = open(file, 'r')
	reader = csv.reader(csvfile)

	for n,row in enumerate(reader):
	    if n == 0:
	        for element in row:
	            print element
	    else:
	        print row

	csvfile.close()

if __name__ == "__main__":
	file = raw_input("enter the name of CSV file to import: ")
	import_csv(file)
