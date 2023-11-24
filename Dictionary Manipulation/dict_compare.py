# This script is designed to check if words in a given text file are English words. 
# It compares each word in the file against a list of English words, which can be either from the NLTK corpus or a custom dictionary provided by the user. 
# The script outputs a list of non-English words found in the text file.

import argparse
import nltk

# Function to check if a word is an English word
def is_english_word(word, english_words):
    return word.lower() in english_words

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Compare words in a file against an English dictionary.')
    parser.add_argument('input_file', type=str, help='Path to the input file containing text strings')
    parser.add_argument('--custom_dict', type=str, help='Path to a custom dictionary file')
    args = parser.parse_args()

    # Load English words
    if args.custom_dict:
        with open(args.custom_dict, 'r') as file:
            english_words = set(word.strip().lower() for word in file)
    else:
        nltk.download('words')
        from nltk.corpus import words
        english_words = set(words.words())

    # Read the input file and compare each word
    with open(args.input_file, 'r') as file:
        non_english_words = [word.strip() for word in file if not is_english_word(word.strip(), english_words)]

    # Write non-English words to a new file
    with open('non_english_words.txt', 'w') as new_file:
        for word in non_english_words:
            new_file.write(word + '\n')

    print("Non-English words have been saved to non_english_words.txt")

if __name__ == "__main__":
    main()
