import itertools
import sys
import argparse

def predict_permutations(string, leetspeak_dict):
    """
    Predicts the total number of leetspeak permutations for a given string.
    """
    total_permutations = 1
    for char in string:
        if char in leetspeak_dict:
            total_permutations *= len(leetspeak_dict[char])
        else:
            total_permutations *= 1
    return total_permutations

def format_file_size(size_bytes):
    """
    Formats file size in appropriate units: KB, MB, GB, or TB.
    """
    if size_bytes >= 1024 ** 4:
        return f"{size_bytes / (1024 ** 4):.2f} TB"
    elif size_bytes >= 1024 ** 3:
        return f"{size_bytes / (1024 ** 3):.2f} GB"
    elif size_bytes >= 1024 ** 2:
        return f"{size_bytes / (1024 ** 2):.2f} MB"
    elif size_bytes >= 1024:
        return f"{size_bytes / 1024:.2f} KB"
    else:
        return f"{size_bytes} Bytes"

def estimate_file_size(total_permutations, avg_length):
    """
    Estimates the size of the output file based on total permutations and average length of a string.
    """
    return total_permutations * (avg_length + 1)  # Include newline character

def generate_leetspeak_combinations(word, leetspeak_dict):
    """
    Generates leetspeak combinations lazily to reduce memory usage.
    """
    word_variations = (
        leetspeak_dict[char] if char in leetspeak_dict else [char]
        for char in word
    )
    for combo in itertools.product(*word_variations):
        yield ''.join(combo)

def main():
    parser = argparse.ArgumentParser(description="A leetspeak generator that takes an input string and generates all possible leetspeak variations.")
    parser.add_argument('-i', '--input', type=str, help="Input string containing up to three words, separated by spaces. For multiple words, wrap in quotes.")
    parser.add_argument('-o', '--output', type=str, help="Output file name. If not specified, output will be printed to the screen.")
    args = parser.parse_args()

    leetspeak_dict = {
        'a': ['4', '@', 'A', 'a'],
        'b': ['8', 'B', 'b'],
        'c': ['(', 'C', 'c'],
        'd': ['D', 'd', '|)', '|]'],
        'e': ['3', 'E', 'e'],
        'f': ['F', 'f'],
        'g': ['6', 'G', 'g'],
        'h': ['#', 'H', 'h'],
        'i': ['1', '!', 'I', 'i'],
        'j': ['J', 'j'],
        'k': ['K', 'k'],
        'l': ['1', 'L', 'l'],
        'm': ['M', 'm'],
        'n': ['N', 'n'],
        'o': ['0', 'O', 'o'],
        'p': ['P', 'p'],
        'q': ['Q', 'q'],
        'r': ['R', 'r'],
        's': ['5', '$', 'S', 's'],
        't': ['7', 'T', 't'],
        'u': ['U', 'u', '|_|'],
        'v': ['V', 'v'],
        'w': ['W', 'w'],
        'x': ['X', 'x'],
        'y': ['Y', 'y'],
        'z': ['Z', 'z'],
        ' ': ['-', '_', ' '],
    }

    if args.input:
        input_string = args.input.strip()
    else:
        input_string = input("Enter input string (up to 3 words): ").strip()

    # Calculate total permutations
    total_permutations = predict_permutations(input_string, leetspeak_dict)
    avg_length = len(input_string)
    estimated_size = estimate_file_size(total_permutations, avg_length)
    formatted_size = format_file_size(estimated_size)

    # Interactive mode: Confirm before proceeding
    if not args.input:
        print(f"Total permutations: {total_permutations}")
        print(f"Estimated file size: ~{formatted_size}")
        proceed = input("Do you want to continue? (y/n): ").strip().lower()
        if proceed != 'y':
            print("Operation aborted.")
            sys.exit(0)

    # CLI mode: Print stats
    elif args.input:
        print(f"Total permutations: {total_permutations}")
        print(f"Estimated file size: ~{formatted_size}")

    # Generate and output combinations
    if args.output:
        with open(args.output, 'w') as f:
            for combo in generate_leetspeak_combinations(input_string, leetspeak_dict):
                f.write(combo + '\n')
        print(f"Permutations written to {args.output}")
    else:
        for combo in generate_leetspeak_combinations(input_string, leetspeak_dict):
            print(combo)

if __name__ == "__main__":
    main()
