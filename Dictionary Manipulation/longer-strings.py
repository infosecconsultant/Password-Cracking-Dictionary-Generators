# This script extracts and categorizes strings from a given text file into two categories: letters and non-letters. 
# Each category is saved in a separate output file.



import argparse
import re

def extract_strings(input_file, output_file_letters, output_file_others):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file_letters, 'w') as file_letters, open(output_file_others, 'w') as file_others:
        for line in lines:
            # Split the line into sequences of letters and non-letters
            sequences = re.findall(r'([a-zA-Z]+|[^a-zA-Z]+)', line)

            for seq in sequences:
                if re.match(r'[a-zA-Z]+', seq):
                    # Write to letters file
                    file_letters.write(seq + '\n')
                else:
                    # Write to others file
                    file_others.write(seq + '\n')

def main():
    parser = argparse.ArgumentParser(description='Extract and categorize strings into letters and non-letters.')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('output_file_letters', type=str, help='Path to the output file for letters')
    parser.add_argument('output_file_others', type=str, help='Path to the output file for non-letters')
    args = parser.parse_args()

    extract_strings(args.input_file, args.output_file_letters, args.output_file_others)

if __name__ == "__main__":
    main()
