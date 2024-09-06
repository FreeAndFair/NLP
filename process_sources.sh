#!/bin/sh

# Phrases Processing Script
# Daniel M. Zimmerman, September 2024

# This script recursively traverses the supplied directory, processing all
# files within it using the phrases scripts. It assumes that the files all
# have unique basenames, even if they're in different directories.

# Check if exactly one argument is passed
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Check if the argument is a directory
if [ ! -d "$1" ]; then
    echo "Error: '$1' is not a directory."
    exit 1
fi

echo "Generating histograms for all dependent documents that don't have them."
echo "Scanning directory $1."

find "$1" -follow -type f | while IFS= read -r file; do
	base=`basename $file`
	# We don't care about the file extension, we're just going to assume we
	# can process it.
	noext=${base%.*}
	# Don't process a README
	if [ ${noext} = "README" ]; then 
		continue
	fi
	echo "Processing ${noext}..."
	nounsfile="raw_output/${noext}_nouns.csv"
	verbsfile="raw_output/${noext}_verbs.csv"
	if [ -f ${nounsfile} ]; then 
		echo "  ${noext} nouns histogram already exists"
	else
		echo "  Creating nouns histogram..."
		phrases/nouns.py ${file} > ${nounsfile}
	fi
	if [ $? -ne 0 ]; then
		rm -f ${nounsfile}
    echo "Processing of ${noext} failed, exiting."
		exit 1
	fi
	if [ -f ${verbsfile} ]; then
		echo "  ${noext} verbs histogram already exists"
	else
		echo "  Creating verbs histogram..."
		phrases/verbs.py ${file} > ${verbsfile}
	fi
	if [ $? -eq 0 ]; then
    echo "Processing of ${noext} complete."
	else
		rm -f ${verbsfile}
    echo "Processing of ${noext} failed, exiting."
		exit 1
	fi
done
