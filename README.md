# prake
Python Implementation of Rapid Automatic Keyword Extraction (RAKE)

### Description

RAKE (Rapid Automatic keyword Extraction) is an algorithm for the extraction of keywords designed
to be extremely efficient, to operate on single documents and heterogeneous sets of documents.

The original algorithm has been developed by Stuart Rose, Dave Engel, Nick Cramer and Wendy Cowley
and published in the book "Text Mining: Applications and Theory"

### Installation

Clone the repository in your favourite location:
```
$ git clone https://github.com/vitaled/prake
```
Then execute the installation script:

```
$ python setup.py install
```

### Usage

prake can be used has as a library:

**Example:**

```python
from prake import Extractor

extractor = Extractor() #Default lang is "en"
keywords  = extractor.extract_keywords(text_sample)
```

The package also provide the script *extract-keywords.py* that can be used to extract keywords from a text file and save them to an other file

**Example:**

Extracting keywords from the file *nyt.txt* and save them into the file *nyt.txt.keywords*

```
$ extract-keywords.py -l en --i nyt.txt --o nyt.txt.keywords
```

### References
Rose S., Engel D., Cramer N. and Cowley W. [Automatic Keyword Extraction from Individual Documents](https://www.researchgate.net/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents) (*Text Mining: Applications and Theory pp 1-20*)
