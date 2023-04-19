# Leetspeak Generator

A Python-based leetspeak generator that takes an input string of up to three words and generates all possible leetspeak variations.

## Overview

Leetspeak, also known as 1337 or leet, is an alternative alphabet used primarily on the internet. It uses various combinations of ASCII characters to replace certain letters. This tool allows you to generate all possible leetspeak variations of an input string containing up to three words.

## Features

- Accepts input of up to three words, separated by spaces
- Supports command line arguments for direct input and help message
- Generates all possible leetspeak variations for the given input string, including spaces

## How to Use

1. Ensure you have Python installed on your system.
2. Download the leetspeak-generator.py script from this repository.
3. Open a terminal or command prompt and navigate to the directory containing the script.

### Interactive Mode (default)

- Run the script using the following command: `python leetspeak-generator.py`
- When prompted, enter your input string containing up to three words, separated by spaces.
- The script will generate and display all possible leetspeak variations of the input string.

### Direct Input Mode

- Run the script with the input string directly using the following command: `python leetspeak-generator.py -i "words here"`
- The script will generate and display all possible leetspeak variations of the input string.

### Display Help Message

- Run the script with the `-h` flag to display the help message: `python leetspeak-generator.py -h`

## Customization

The leetspeak character substitutions are defined in a dictionary within the script. You can easily update or modify the dictionary to include additional characters or alternative substitutions as needed.
