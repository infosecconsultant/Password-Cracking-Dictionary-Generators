# This script is designed to extract and sort strings of 3 characters or less from a given text file. 
# It reads an input file, filters out strings that exceed 3 characters in length, writes the short strings to an output file, and then sorts these strings uniquely.

import argparse
import subprocess

def extract_short_strings(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Strip leading/trailing whitespace and check if the length is 3 or less
            if len(line.strip()) <= 3:
                outfile.write(line)

def main():
    parser = argparse.ArgumentParser(description='Extract strings of 3 characters or less from a file.')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('output_file', type=str, help='Path to the output file')
    args = parser.parse_args()

    extract_short_strings(args.input_file, args.output_file)
    subprocess.run(['sort', '-u', args.output_file, '-o', args.output_file])
    print(f"Strings of 3 characters or less have been extracted to {args.output_file}")

if __name__ == "__main__":
    main()
