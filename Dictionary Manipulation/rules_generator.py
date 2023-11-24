# This script is designed to generate Hashcat rules from strings in a given text file. 
# It reads each line from the input file, creates prefix and suffix rules for Hashcat, and then writes these rules to an output file. 
# The script is particularly useful for creating custom rules for password cracking or testing in Hashcat.


import argparse

def convert_to_hashcat_rules(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    prefix_rules = []
    suffix_rules = []

    for line in lines:
        line = line.strip()
        prefix_rule = ''.join([f'^{char}' for char in line])
        suffix_rule = ''.join([f'${char}' for char in line])

        prefix_rules.append(prefix_rule)
        suffix_rules.append(suffix_rule)

    return prefix_rules, suffix_rules

def write_rules_to_file(prefix_rules, suffix_rules, output_file):
    with open(output_file, 'w') as file:
        file.write("# Prefix Rules\n")
        for rule in prefix_rules:
            file.write(rule + '\n')

        file.write("\n# Suffix Rules\n")
        for rule in suffix_rules:
            file.write(rule + '\n')

def main():
    parser = argparse.ArgumentParser(description='Generate Hashcat rules from strings in a file.')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('output_file', type=str, help='Path to the output file')
    args = parser.parse_args()

    prefix_rules, suffix_rules = convert_to_hashcat_rules(args.input_file)
    write_rules_to_file(prefix_rules, suffix_rules, args.output_file)

if __name__ == "__main__":
    main()

