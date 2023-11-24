# This script is designed to extract and categorize different types of string sequences from a given text file. 
# It categorizes strings into four categories: letters, short letters, numbers, and special characters. 
# Each category is saved in a separate output file, and the contents of these files are sorted and deduplicated.

import re
import subprocess

def extract_strings(input_file, output_files):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    file_handles = {key: open(file, 'w') for key, file in output_files.items()}

    for line in lines:
        # Split the line into sequences of letters, digits, and others
        sequences = re.findall(r'([a-zA-Z]+|\d+|[^a-zA-Z\d]+)', line)

        for seq in sequences:
            if re.match(r'[a-zA-Z]{3,}', seq):
                file_handles['letters'].write(seq + '\n')
            elif re.match(r'[a-zA-Z]{1,2}', seq):
                file_handles['short_letters'].write(seq + '\n')
            elif re.match(r'\d+', seq):
                file_handles['numbers'].write(seq + '\n')
            elif re.match(r'[^a-zA-Z\d]+', seq):
                file_handles['specials'].write(seq + '\n')

    # Close all file handles
    for file in file_handles.values():
        file.close()

    # Sort and remove duplicates in each file
    for file in output_files.values():
        subprocess.run(['sort', '-u', file, '-o', file])

# Example usage
input_file = 'input.txt'  # Replace with your input file path
output_files = {
    'letters': 'letters.txt',
    'specials': 'specials.txt',
    'short_letters': 'short_letters.txt',
    'numbers': 'numbers.txt'
}
extract_strings(input_file, output_files)
