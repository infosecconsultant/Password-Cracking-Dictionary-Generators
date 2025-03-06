import itertools
import argparse
import sys

def generate_permutations(word):
    return map(''.join, itertools.product(*((c.upper(), c.lower()) for c in word)))

def process_word(word, output_handle=None):
    # Generate the permutations for the word
    perms = generate_permutations(word)
    header = f"Permutations for word: {word}\n"
    if output_handle:
        output_handle.write(header)
        for p in perms:
            output_handle.write(p + '\n')
        output_handle.write('\n')
    else:
        print(header, end='')
        for p in perms:
            print(p)
        print()

def main():
    parser = argparse.ArgumentParser(
        description="Generate case permutations for words."
    )
    # Create a mutually exclusive group for word vs file input.
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-w", "--word", help="Input word")
    group.add_argument("-f", "--file", help="File containing list of words (one per line)")
    parser.add_argument("-o", "--output", help="Output file to write permutations", type=str)
    
    args = parser.parse_args()
    
    # Determine output handle if an output file is provided
    output_handle = None
    if args.output:
        try:
            output_handle = open(args.output, 'w')
        except Exception as e:
            print(f"Error opening output file {args.output}: {e}")
            sys.exit(1)

    # Process a single word if provided via -w
    if args.word:
        process_word(args.word, output_handle)
    # Process words from a file if provided via -f
    elif args.file:
        try:
            with open(args.file, 'r') as f:
                for line in f:
                    word = line.strip()
                    if word:  # skip empty lines
                        process_word(word, output_handle)
        except Exception as e:
            print(f"Error reading file {args.file}: {e}")
            sys.exit(1)
    # Otherwise, prompt the user interactively for a word
    else:
        word = input("Please enter the word: ").strip()
        if word:
            process_word(word, output_handle)
        else:
            print("No valid input provided.")
            sys.exit(1)

    if output_handle:
        output_handle.close()
        print(f"Permutations written to {args.output}")

if __name__ == "__main__":
    main()
