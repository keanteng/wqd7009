import os
import re

# Directory containing the files
directory = 'data/ori'

# Regular expression to match the file names
pattern = re.compile(r'seoul (\d{4}-\d{2}-\d{2}) to (\d{4}-\d{2}-\d{2})')

# Iterate over all files in the directory
for filename in os.listdir(directory):
    match = pattern.match(filename)
    if match:
        # Extract the years from the matched groups
        year1 = match.group(1)[:4]
        year2 = match.group(2)[:4]
        # Create the new file name
        new_filename = f'seoul_{year1}_{year2}.csv'
        # Get the full file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {old_file} to {new_file}')