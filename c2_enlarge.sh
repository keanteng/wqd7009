#!/bin/bash

# Source file
src_file="data/enlarge/data_large.csv"

# Destination directory
dest_dir="data/enlarge/2"

# Create the destination directory if it doesn't exist
mkdir -p "$dest_dir"

# Duplicate the file 200 times
for i in {1..200}; do
    cp "$src_file" "$dest_dir/data_large_c2_$i.csv"
done

echo "Done"