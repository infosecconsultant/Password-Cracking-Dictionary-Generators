import itertools

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
    leetspeak_dict = {
		'a': ['4', '@', 'A', 'a'],
		'b': ['8', 'B', '|3', 'b'],
		'c': ['(', '[', '{', '<', 'C', 'c'],
		'd': ['|)', '|]', 'D', 'd'],
		'e': ['3', 'E', 'e'],
		'f': ['|=', 'F', 'f'],
		'g': ['6', '9', 'G', 'g'],
		'h': ['#', '|-|', 'H', 'h'],
		'i': ['1', '!', '|', 'I', 'i'],
		'j': ['_|', 'J', 'j'],
		'k': ['|<', 'K', 'k'],
		'l': ['1', '|_', 'L', 'l'],
		'm': ['|\\/|', 'M', '|\\\/|', 'm'],
		'n': ['|\\|', 'N', 'n'],
		'o': ['0', 'O', 'o'],
		'p': ['|D', '|o', 'P', 'p'],
		'q': ['(,)', 'Q', 'q'],
		'r': ['|2', 'R', 'r'],
		's': ['5', '$', 'S', 's'],
		't': ['7', '+', 'T', 't'],
		'u': ['|_|', 'U', 'u'],
		'v': ['\\/', 'V', 'v'],
		'w': ['\\|/', '\\^/', 'W', '\\\/\\\/', 'w'],
		'x': ['%', '><', 'X', 'x'],
		'y': ['`/', 'Y', 'y'],
		'z': ['2', 'Z', 'z'],
	    ' ': ['-', '_', ' '],
    }

    input_string = prompt_user_input()
    combinations = generate_leetspeak_combinations(input_string, leetspeak_dict)
    for combo in combinations:
        print("".join(combo))

if __name__ == "__main__":
    main()
