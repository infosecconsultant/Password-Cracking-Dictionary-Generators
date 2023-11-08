import itertools
import sys

def generate_permutations(word):
    return map(''.join, itertools.product(*((c.upper(), c.lower()) for c in word)))

def main():
    # Check if a word was provided as a command-line argument
    if len(sys.argv) >= 2:
        word = sys.argv[1]
    else:
        # Prompt the user for a word if not supplied as an argument
        word = input("Please enter the word: ")
    
    # Check if an output file was provided as a command-line argument
    output_file = sys.argv[2] if len(sys.argv) >= 3 else None

    permutations = generate_permutations(word)
    
    if output_file:
        # Write the permutations to the output file
        with open(output_file, 'w') as f:
            for perm in permutations:
                f.write(perm + '\n')
        print(f"Permutations written to {output_file}")
    else:
        # Print the permutations to the screen
        for perm in permutations:
            print(perm)

if __name__ == "__main__":
    main()
