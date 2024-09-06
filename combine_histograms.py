#!/usr/bin/env python
"""
CSV Histogram Combiner
Daniel M. Zimmerman, September 2024

Usage:
$ ./combine_histograms.py <directory> <type>

Takes all the <type>.csv files in <directory>, which are assumed to be
histograms with terms (the first column) and frequencies (the second
column), and generates a single <type>.csv file combining all terms and
frequencies. This script does _not_ attempt to aggregate "similar"
terms or do any other clever optimizations when combining the
histograms; if Python thinks two terms are equivalent, their
frequencies are aggregated, and if it doesn't, they aren't.
"""

import sys
import csv
import os

class MalformedFile(Exception):
    pass

def process_csv_file(file_path, histogram):
    """Read a CSV file and update the histogram with its counts."""
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=['freq', 'term'], restkey='rest', delimiter='\t')
            for row in reader:
                if (row['freq'] == None or row['term'] == None or 'rest' in row):
                    raise MalformedFile
                else:
                    new_freq = int(row['freq'])
                    if row['term'] in histogram:
                        new_freq = histogram[row['term']] + new_freq
                    histogram[row['term']] = new_freq
    except MalformedFile:
        print(f"Error processing {file_path}: incorrect number of columns")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def generate_output_file(histogram, histogram_type):
    """Generate a <histogram_type>.csv file containing the histogram."""
    # using negative numbers to sort phrases with
    # more occurrences ahead of those with fewer
    sorted_histogram = sorted([(0 - n, phrase) for (phrase, n) in histogram.items()])

    # if we've gotten here, we don't check for overwriting the file - that check
    # happens before we process anything

    f = open(f"{histogram_type}.csv", "a")
    for (n, p) in sorted_histogram:
        print("%u\t%s" % (0 - n, p), file=f)
    f.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./combine_raw_output.py <directory> <type>")
        sys.exit(1)

    input_path = sys.argv[1]
    histogram_type = sys.argv[2]

    # check for existing output file
    if os.path.isfile(f'{histogram_type}.csv'):
        print(f'{histogram_type}.csv already exists, aborting.')
        sys.exit(1)

    # check for directory
    if os.path.isdir(input_path):
        # process all csv files
        combined_histogram = {}
        files_processed = 0
        for file_name in os.listdir(input_path):
            file_path = os.path.join(input_path, file_name)
            # Check if it's a .csv file
            if os.path.isfile(file_path) and file_name.endswith(f'{histogram_type}.csv'):
                files_processed = files_processed + 1
                process_csv_file(file_path, combined_histogram)
        print(f'{files_processed} files processed')
        generate_output_file(combined_histogram, histogram_type)
    else:
        print(f"'{input_path}' is not a directory.")
        sys.exit(1)
