all: selftest

selftest: README-nouns.csv README-verbs.csv

README-nouns.csv: README.md
	nouns.py README.md > README-nouns.csv;
	diff README-nouns.csv README-nouns.csv.out;

README-verbs.csv: README.md
	verbs.py README.md > README-verbs.csv;
	diff README-verbs.csv README-verbs.csv.out;

extract_baseline:
	nouns.py README.md > README-nouns.csv.out;
	verbs.py README.md > README-verbs.csv.out;

clean:
	rm -f README-nouns.csv;
	rm -f README-verbs.csv;
