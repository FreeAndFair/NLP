# Extracting noun phrases from documents

Requirements:
- input is either a stdin pipe or a filename
- if the input file is not plain text, convert it to such
- the input file can be PDF, Unicode, or ASCII
- output is a histogram of noun and verb phrases, complete with
  adjective and adverbial modifiers, contained in the input

This script uses [TextBlob](https://textblob.readthedocs.io/en/dev/)
for the heavy lifting.

## Installation

This tool depends upon Python2 and a few C and Python libraries.  See
the first step below.

Note that one must be careful about OS X installations, given the
built-in Python2 is not a satisfactory version for this tooling. We
recommend replacing the built-in Python2 with brew's via `pyenv`.

0. Install distribution-level dependencies (Ubuntu/Debian example here)
 - `$ sudo apt install build-essential libpoppler-cpp-dev pkg-config
   python3-venv`
1. `brew install pyenv pyenv-virtualenv` (v2.4.10 is latest as of this writing)
3. `pyenv install 3.12.5` (v3.12.5 is the latest release of Python3)
4. `pyenv install 2.7.18` (v2.7.18 is the final release of Python2)
5. `pyenv global system 3.12.5 2.7.18` (puts both versions into the
   global environment)
2. Run `eval "$(pyenv init -)"` and consider adding it to your shell
   startup.
6. Create a Python [virtual environment](https://docs.python.org/3/library/venv.html)
 - `$ python3 -m venv env` makes one named `env`
 - `$ source env/bin/activate` lets you work in that environment
 - `$ deactivate` gets you back to your normal environment 
3. Install Python package dependencies, making sure you use Python2's pip:
 - `$ pip2 install -r requirements.txt`
5. Install Pattern locally
 - `$ pip2 install -e pattern-2.6`
6. Download necessary NLTK data
 - `$ python2 -c 'import nltk; nltk.download("brown"); nltk.download("punkt")'`
 - `$ python2 -m textblob.download_corpora`

### Testing the Installation

The provided `Makefile` has two rules which run the extraction
commands on this README.  If those commands run with no output beyond
printing the selftest commands, the installation is working.

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

- [Pattern package documentation](https://www.clips.uantwerpen.be/pages/pattern-en#parser)
- [tags explained](https://www.clips.uantwerpen.be/pages/mbsp-tags)
- [TextBlob tutorial](http://rwet.decontextualize.com/book/textblob/)
