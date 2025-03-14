#!/usr/bin/env python
'''
See README.md for setup.

Usage:
$ ./verbs.py $DOCUMENT
$ ./verbs.py -          (Expect input via stdin)

Works with PDF, UTF-8, and ASCII documents.

Outputs tab-delimited histogram of verb phrase count.
'''
from pattern.en import parsetree

import sys
import magic
import pdftotext

if len(sys.argv) == 2:
    filename = sys.argv[1]
    input_text = None
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

if input_text == None:
    print("No text read from input, skipping.")
    exit(0)

s = parsetree(input_text)

hist = {}

for sentence in s:
    for chunk in sentence.chunks:
        if chunk.type == 'VP':
            c = chunk.string.lower()
            if c in hist:
                hist[c] += 1
            else:
                hist[c] = 1

# using negative numbers to sort phrases with
# more occurrences ahead of those with fewer
sorted_hist = sorted([(0 - n, phrase) for (phrase, n) in hist.items()], 
               key = lambda x: (x[0], x[1]))

for (n, p) in sorted_hist:
    print("%u\t%s" % (0 - n, p))
