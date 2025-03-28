import argparse
import itertools

def load_words_from_dict(file_path):
    """Load words from a dictionary file (one word per line)."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            # Strip whitespace and skip empty lines
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        raise RuntimeError(f"Error reading {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Generate a wordlist of all permutations of input words."
    )
    parser.add_argument(
        "-i", "--input",
        help="Comma separated list of words (e.g. 'cat,bird,dog').",
        default=None
    )
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Output file path where the wordlist will be saved."
    )
    parser.add_argument(
        "-d", "--delimiter",
        default="",
        help="Delimiter to use between words. If not specified, words are concatenated without a delimiter."
    )
    parser.add_argument(
        "-p", "--prepend",
        default="",
        help="Static string to prepend to each output value."
    )
    parser.add_argument(
        "--dict1",
        help="Path to dictionary file 1 (one word per line).",
        default=None
    )
    parser.add_argument(
        "--dict2",
        help="Path to dictionary file 2 (one word per line).",
        default=None
    )
    parser.add_argument(
        "--dict3",
        help="Path to dictionary file 3 (one word per line).",
        default=None
    )
    args = parser.parse_args()

    # Determine the source of words.
    if args.dict1 or args.dict2 or args.dict3:
        words = []
        for dict_file in (args.dict1, args.dict2, args.dict3):
            if dict_file:
                words.extend(load_words_from_dict(dict_file))
    elif args.input:
        words = args.input.split(',')
    else:
        parser.error("You must provide either a comma separated input (-i) or at least one dictionary file (--dict1, --dict2, --dict3).")
    
    # Generate all possible permutations of the input words.
    permutations = itertools.permutations(words, len(words))

    # Write each permutation to the output file with optional prepend and delimiter.
    with open(args.output, "w", encoding="utf-8") as f:
        for perm in permutations:
            line = args.prepend + args.delimiter.join(perm)
            f.write(line + "\n")

if __name__ == "__main__":
    main()
