import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Swap case for each letter in the input words.')
parser.add_argument('-i', '--input', type=str, help='Input file containing words, one per line.', required=True)
parser.add_argument('-o', '--output', type=str, help='Output file to write the swapped case words.')

# Parse arguments
args = parser.parse_args()

# Open the input file
with open(args.input, 'r') as infile:
    # If an output file is specified, open it; otherwise, set output to None
    outfile = open(args.output, 'w') if args.output else None

    # Process each line from the input file
    for line in infile:
        swapped_line = line.strip().swapcase()

        # Write to the output file if specified, otherwise print to stdout
        if outfile:
            outfile.write(swapped_line + '\n')
        else:
            print(swapped_line)

# Close the output file if it was opened
if outfile:
    outfile.close()
