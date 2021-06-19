#!/bin/bash

for file in *.csv; do
    [ -f "$file" ] || continue
	for file1 in *.csv; do
		[ -f "$file1" ] || continue
		python UTR3Comparison.py "$file" "$file1"
	done
	for file1 in *.csv; do
		[ -f "$file1" ] || continue
		python common_variations.py "$file" "$file1"
	done
	for file1 in *.txt; do
		[ -f "$file1" ] || continue
		python common_genes.py "$file" "$file1"
	done
done
