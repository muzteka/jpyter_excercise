# -*- coding: UTF-8 -*-
import pprint
from xml.etree import ElementTree as ET


def import_xml(file):
	tree = ET.parse(file)
	root = tree.getroot()

	data = root.find('Data')

	all_data = []

	for observation in data:
		record = {}
		for item in observation:

			lookup_key = item.attrib.keys()[0]

			if (lookup_key == 'Numeric'):
				rec_key = 'NUMERIC'
				rec_value = item.attrib['Numeric']
			else:
				rec_key = item.attrib[lookup_key]
				rec_value = item.attrib['Code']
			record[rec_key] = rec_value

		all_data.append(record)

	pprint.pprint(all_data)
	

if __name__ == "__main__":
	file = raw_input("enter the name of XML file to import: ")
	import_xml(file)
