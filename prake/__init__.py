import re 
import operator
import os
import codecs

class Extractor:
	
	def  __init__(self,lang=None,stopwords_file=None,phrase_delimiters_file=None,threshold=0.3):
		
		ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 

		# Setting Threshold
		self.threshold = threshold

		# Default Language
	
		if not lang:
			self.lang = "en"
		else:
			self.lang = lang

		if not stopwords_file:
			self.stopwords = self.load_words(ROOT_DIR+"/data/"+self.lang+".stopwords.txt")
		else:
			self.stopwords = self.load_words(stopwords_file)

		if not phrase_delimiters_file:
			self.phrase_delimiters = self.load_words(ROOT_DIR+"/data/"+self.lang+".phrase_delimiters.txt")
		else:
			self.phrase_delimiters = self.load_words(phrase_delimiters_file)

	def extract_keywords(self,text):

		candidate_keywords = []

		freq = {}
		deg  = {}
		last_candidate = []		

		text = text.strip().lower()
    		text = re.sub(r"([\W])"," \g<1> ",text)
    		text = re.sub(r"\s+"," ",text)

    		tokens = re.split(r"[\s]",text)
   
    		for token in tokens:
    
        		if token not in self.stopwords and token not in self.phrase_delimiters and token !='':

            			if token not in freq:
                			freq[token]= 1
            			else:
                			freq[token]+=1
  
            			last_candidate.append(token)
				
		        elif len(last_candidate)>0:
            			candidate_keywords.append(last_candidate)
				# compute degree 
				for keyword in last_candidate:
                			if keyword not in deg:
                    				deg[keyword] = len(last_candidate)-1
                			else:
                    				deg[keyword]+= len(last_candidate)-1
				last_candidate = []

		if(len(last_candidate) > 0):
    				candidate_keywords.append(last_candidate)
				for keyword in last_candidate:
	               			if keyword not in deg:
                    				deg[keyword] = len(last_candidate)-1
                			else:
                    				deg[keyword]+= len(last_candidate)-1

		
		scores = {}
		for ck in candidate_keywords:
    			score = 0.0
	    		for token in ck:
        			score += float(deg[token]+freq[token])/float(freq[token])
    				scores[" ".join(ck)] = score

    		return sorted(scores.items(),key=operator.itemgetter(1),reverse=True)[0:int(len(scores)*self.threshold)]

	def load_words(self,path):
		f = codecs.open(path,"r","utf-8")
    		words = set()
    		for line in f:
        		words.add(line.strip())
    		f.close()
    		return words

