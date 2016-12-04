#!/usr/bin/python
# -*- coding: utf8 -*-
import argparse
import codecs
import os
from prake import Extractor

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Extract keywords from a given text')
	parser.add_argument('-l','--lang',default='en')
	parser.add_argument('-i','--input',required=True)
	parser.add_argument('-o','--output')
	args = parser.parse_args()

	extractor = Extractor(lang=args.lang)

	input_file_name = args.input

	input_file = codecs.open(input_file_name,"r","utf-8")

	output_file_version  = 1
	output_file_basename = os.path.basename(input_file_name)+'.keywords'
	output_file_name     = output_file_basename
	while os.path.isfile(output_file_name):
		output_file_name = output_file_basename+'.'+str(output_file_version)
		output_file_version+=1		
	output_file= codecs.open(output_file_name,"w","utf-8")

	text_sample = ""

	for line in input_file:
        	text_sample+=' '+line.strip()

	for keyword in extractor.extract_keywords(text_sample):
        	output_file.write(keyword[0])
		output_file.write("\n")
	input_file.close()
	output_file.close()	 
