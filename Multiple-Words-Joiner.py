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
        description="Generate a wordlist of combinations from input words or dictionary files."
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

    # If any dictionary files are provided, use them in a Cartesian product.
    if args.dict1 or args.dict2 or args.dict3:
        dict_lists = []
        for dict_file in (args.dict1, args.dict2, args.dict3):
            if dict_file:
                words = load_words_from_dict(dict_file)
                dict_lists.append(words)
        # Produce every possible combination: one word from each provided dictionary.
        combinations = itertools.product(*dict_lists)
    elif args.input:
        words = args.input.split(',')
        # Produce all possible permutations of the comma-separated words.
        combinations = itertools.permutations(words, len(words))
    else:
        parser.error("You must provide either a comma separated input (-i) or at least one dictionary file (--dict1, --dict2, or --dict3).")
    
    # Write each combination/permutation to the output file with optional prepend and delimiter.
    with open(args.output, "w", encoding="utf-8") as f:
        for combo in combinations:
            line = args.prepend + args.delimiter.join(combo)
            f.write(line + "\n")

if __name__ == "__main__":
    main()
