# -*- coding: UTF-8 -*-

import json
import pprint


def import_json(file):
	json_data = open(file).read()
	data = json.loads(json_data)

	for item in data:
		pprint.pprint(item)

	

if __name__ == "__main__":
	file = raw_input("enter the name of JSON file to import: ")
	import_json(file)
