# Extracting noun/verb phrases from documents

Requirements:
- input is either a stdin pipe or a filename
- if the input file is not plain text, convert it to such
- the input file can be PDF, Unicode, or ASCII
- output is a histogram of noun and verb phrases, complete with
  adjective and adverbial modifiers, contained in the input

These scripts use [TextBlob](https://textblob.readthedocs.io/en/dev/) and [PatternLite](https://github.com/WZBSocialScienceCenter/patternlite) for the heavy lifting.

## Installation

This tool depends upon Python 3 and a few C and Python libraries. On macOS, these instructions assume a working [Homebrew](https://brew.sh) installation. You can choose to use a Python [virtual environment](https://docs.python.org/3/library/venv.html) to install the Python dependencies and run the scripts, but we do not provide explicit instructions for that here.


1. Install distribution-level dependencies
  - Ubuntu/Debian: `$ sudo apt install build-essential libpoppler-cpp-dev libmagic-dev 
   pkg-config python3-pip`
  - macOS: `$ brew install poppler libmagic python3`
2. Install Python package dependencies:
 - `$ pip3 install -r requirements.txt`
3. Download necessary NLTK data
 - `$ python3 -c 'import nltk; nltk.download("brown"); nltk.download("punkt")'`
 - `$ python3 -m textblob.download_corpora`

### Testing the Installation

The provided `Makefile` has a `selftest` target that runs the extraction commands on this `README`.  If those commands run with no output beyond printing the self-test commands, the installation is working.

## Usage

### Extracting Noun Phrases

- `$ ./nouns.py $PDF_OR_TEXT_DOCUMENT.txt > out.csv` or
- `$ ./nouns.py $PDF_OR_TEXT_DOCUMENT.pdf > out.csv` or
- `$ cat $TEXT_DOCUMENT | ./nouns.py - > out.csv`

### Extracting Verb Phrases
- `$ ./verbs.py $PDF_OR_TEXT_DOCUMENT.txt > out.csv` or
- `$ ./verbs.py $PDF_OR_TEXT_DOCUMENT.pdf > out.csv` or
- `$ cat $TEXT_DOCUMENT | ./verbs.py - > out.csv`

## Useful Links

- [Original Pattern package](https://github.com/clips/pattern)
- [TextBlob tutorial](http://rwet.decontextualize.com/book/textblob/)
