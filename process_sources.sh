#!/bin/sh

echo "Generating histograms for all dependent documents that don't have them."

for file in source_docs/*
do
	base=`basename $file`
	# We don't care about the file extension, we're just going to assume we
	# can process it.
	noext=${base%.*}
	# Don't process the README for the source_docs directory
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
	if [ -f ${verbsfile} ]; then
		echo "  ${noext} verbs histogram already exists"
	else
		echo "  Creating verbs histogram..."
		phrases/verbs.py ${file} > ${verbsfile}
	fi
	echo "Processing of ${noext} complete."
done
