import itertools
import sys
import argparse

def prompt_user_input():
    user_input = ""
    while True:
        user_input = input("Please enter a word or words (up to 3 words): ").strip()
        words = user_input.split()
        word_count = len(words)

        if word_count > 0 and word_count <= 3:
            break
        else:
            print("Invalid input. Please enter 1 to 3 words.")

    return user_input

def generate_leetspeak_combinations(word, leetspeak_dict):
    word_variations = []
    for char in word:
        if char in leetspeak_dict:
            word_variations.append(leetspeak_dict[char])
        else:
            word_variations.append([char])

    return list(itertools.product(*word_variations))

def main():
    parser = argparse.ArgumentParser(description="A leetspeak generator that takes an input string of up to three words and generates all possible leetspeak variations.")
    parser.add_argument('-i', '--input', type=str, help="Input string containing up to three words, separated by spaces. For multiple words, wrap in quotes")
    parser.add_argument('-o', '--output', type=str, help="Output file name. If not specified, output will be printed to the screen")
    args = parser.parse_args()



    leetspeak_dict = {
                'a': ['4', '@', 'A', 'a', '/\\', '/-\\'],
                'b': ['8', 'B', '|3', 'b', '13', '!3', '6', 'I3', '!3', '/3'],
                'c': ['(', '[', '{', '<', 'C', 'c'],
                'd': ['|)', '|]', 'D', 'd', 'cl', 'cI', 'I)', 'I]'],
                'e': ['3', 'E', 'e', '[-'],
                'f': ['|=', 'F', 'f', '/=', 'I=', 'ph'],
                'g': ['6', '9', 'G', 'g', '(_-', '(_+', 'C-', '[,'],
                'h': ['#', '|-|', 'H', 'h', '|~|', 'I-I', 'I~I', ']-[', ']~[', '}{', ')-(', '(-)', ')~(', '(~)'],
                'i': ['1', '!', '|', 'I', 'i', '[]'],
                'j': ['_|', 'J', 'j'],
                'k': ['|<', 'K', 'k', '|c', 'Ic', '|{', '|('],
                'l': ['1', '|_', 'L', 'l', '|', '7'],
                'm': ['|\\/|', 'M', 'm'],
                'n': ['|\\|', 'N', 'n'],
                'o': ['0', 'O', 'o'],
                'p': ['|D', '|o', 'P', 'p'],
                'q': ['(,)', 'Q', 'q'],
                'r': ['|2', 'R', 'r'],
                's': ['5', '$', 'S', 's'],
                't': ['7', '+', 'T', 't', '-|-', '~|~'],
                'u': ['|_|', 'U', 'u', '(_)', 'L|'],
                'v': ['\\/', 'V', 'v'],
                'w': ['\\/\\/', 'VV', '\\N', '\'//', '\\\'', '\\^/', '(n)', '\\V/', '\\X/', '\\|/', '\\_|_/', '\\_:_/', 'uu', '2u', '\\\\//\\\\//', 'w', 'W'],
                'x': ['%', '><', 'X', 'x'],
	        'y': ['j', '`/', '7', '\\|/', '\\//', 'Y', 'y'],
                'z': ['2', '7_', '-/_', '%', '>', 's', '~/_', '-\\_', '-|_', 'z', 'Z'],
                ' ': ['-', '_', ' '],
    }

    if args.input:
        input_string = args.input
    else:
        input_string = prompt_user_input()

    combinations = generate_leetspeak_combinations(input_string, leetspeak_dict)

    if args.output:
        with open(args.output, 'w') as f:
            for combo in combinations:
                f.write("".join(combo) + '\n')
    else:
        for combo in combinations:
            print("".join(combo))

if __name__ == "__main__":
    main()
