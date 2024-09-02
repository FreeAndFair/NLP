#!/usr/bin/env python2.7
'''
See README.md for setup.

Usage:
$ ./nouns.py $DOCUMENT  
$ ./nouns.py -          (Expect input via stdin)

Works with PDF, UTF-8, and ASCII documents.

Outputs tab-delimited histogram of noun phrase count.
'''
import sys
import re
import magic
import pdftotext
from textblob import TextBlob

if len(sys.argv) == 2:
    filename = sys.argv[1]
    if filename == '-':
      input_text = sys.stdin.read()
    else:
        file_type =  magic.from_file(filename)
        if 'PDF document' in file_type:
            with open(filename, 'rb') as f:
                input_text = "".join(pdftotext.PDF(f)).encode('ascii','ignore').decode('utf-8')
        elif 'UTF-8 Unicode text' in file_type or 'ASCII text' in file_type:
            with open(filename) as f:
                input_text = f.read().encode('ascii','ignore').decode('utf-8')
        else:
            print("Input doesn't appear to be either a PDF or UTF-8 or ASCII text.")
else:
    print("Please specify filename or - for stdin")
    exit(1)

# get rid of ............... in the proposal (typically in the outline section)
input_text = num = re.sub(r'\.{2,}', " ", input_text)

# remove non-alphanumeric characters (not needed after all)
# input_text = ''.join(filter(lambda c: c.isalpha() or c == ' ' or c == '.', input_text))

input_blob = TextBlob(input_text)

# trivial verb phrase processor
tags = input_blob.tags

# get noun phrases count
counts = input_blob.np_counts

# using negative numbers to sort phrases with
# more occurrences ahead of those with fewer
histo = sorted([(0 - n, phrase) for (phrase, n) in counts.items()])

for (n, p) in histo:
    print("%u\t%s" % (0 - n, p))