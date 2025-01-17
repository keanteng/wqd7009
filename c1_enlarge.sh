#!/bin/bash

# Source file
src_file="data/enlarge/data_large.csv"

# Destination directory
dest_dir="data/enlarge/1"

# Create the destination directory if it doesn't exist
mkdir -p "$dest_dir"

# Duplicate the file 15 times
for i in {1..15}; do
    cp "$src_file" "$dest_dir/data_large_c1_$i.csv"
done

echo "Done"