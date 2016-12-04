#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import codecs
from prake import Extractor

test_dir  = '/home/vitaled/projects/Hulth2003/Test'
extractor = Extractor(threshold=0.3)

for filename in os.listdir(test_dir):
	ext_index = filename.find(".abstr")
	if ext_index != -1:
    		print filename
#   		print filename.replace(".abstr",".contr")
		input_file = codecs.open(test_dir+'/'+filename,"r","utf-8")
		text_sample = ""
		for line in input_file:
                	text_sample+=' '+line.strip()
		input_file.close()
		print text_sample
		keywords_rake = []	
		for keyword in extractor.extract_keywords(text_sample):
               		keywords_rake.append(keyword[0])
		keywords_rake.sort()
		print "[RAKE]"
		print keywords_rake

		keywords_contr = []
		input_file = codecs.open(test_dir+'/'+filename.replace(".abstr",".uncontr"),"r","utf-8")
		for line in input_file:
			for keyword in line.split(';'):
				keyword = keyword.strip()
				if keyword != '':
					keywords_contr.append(keyword.lower())
		input_file.close()
		keywords_contr.sort()
		print "[ORI]"
		print keywords_contr		

		intersection = set(keywords_contr).intersection(set(keywords_rake))	
		print "[RESULTS]"
		print list(intersection)
