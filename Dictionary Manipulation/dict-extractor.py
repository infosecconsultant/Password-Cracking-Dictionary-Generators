# This script is designed to process text strings from a given file, identifying and separating known English words (of length 4 or more) from the remaining text. 
# It uses a dictionary of English words, either from the NLTK corpus or a custom dictionary provided by the user. 
# The script outputs two files: one containing the identified known words and another containing the remaining text.

import argparse
import nltk
import subprocess

def find_longest_word(string, english_words, start, memo):
    if start == len(string):
        return []

    if start in memo:
        return memo[start]

    longest_word = None
    for end in range(start + 1, len(string) + 1):
        word = string[start:end]
        if word.lower() in english_words and len(word) >= 4 and (longest_word is None or len(word) > len(longest_word)):
            longest_word = word

    if longest_word:
        remainder = find_longest_word(string, english_words, start + len(longest_word), memo)
        if remainder is not None:
            memo[start] = [longest_word] + remainder
            return memo[start]

    memo[start] = None
    return None

def find_words_in_string(string, english_words):
    memo = {}
    return find_longest_word(string, english_words, 0, memo)

def main():
    parser = argparse.ArgumentParser(description='Split strings into known and unknown parts.')
    parser.add_argument('input_file', type=str, help='Path to the input file containing text strings')
    parser.add_argument('--custom_dict', type=str, help='Path to a custom dictionary file')
    args = parser.parse_args()

    if args.custom_dict:
        with open(args.custom_dict, 'r') as file:
            english_words = set(word.strip().lower() for word in file)
    else:
        nltk.download('words')
        from nltk.corpus import words
        english_words = set(words.words())

    with open(args.input_file, 'r') as file, \
         open('known_words.txt', 'w') as known_file, \
         open('remaining_text.txt', 'w') as remaining_file:
        for line in file:
            words = find_words_in_string(line.strip(), english_words)
            if words:
                known_file.write('\n'.join(words) + '\n')
                remaining = line.strip()
                for word in words:
                    remaining = remaining.replace(word, '', 1)
                if remaining:
                    remaining_file.write(remaining + '\n')
            else:
                remaining_file.write(line)

    # Sorting and removing duplicates from the output files
    subprocess.run(['sort', '-u', 'known_words.txt', '-o', 'known_words.txt'])
    subprocess.run(['sort', '-u', 'remaining_text.txt', '-o', 'remaining_text.txt'])

    print("Process completed. Check 'known_words.txt' and 'remaining_text.txt'.")

if __name__ == "__main__":
    main()
