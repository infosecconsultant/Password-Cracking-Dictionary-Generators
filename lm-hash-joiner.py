import argparse

def load_pot_file(pot_file):
    """Load the POT file into a dictionary mapping LM hash halves to plaintexts.

    Expected format (each line in the file):
        LM_HASH_HALF:PLAINTEXT
    Example:
        299BD128C1101FD6:PASSWORD
        D9D99F2F2B43B62F:1234567

    Returns:
        dict: A dictionary where keys are LM hash halves (uppercase) and values are plaintext passwords.
    """
    pot_dict = {}
    with open(pot_file, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(':', 1)
            if len(parts) == 2:
                lm_half, plaintext = parts
                pot_dict[lm_half.upper()] = plaintext  # Store in uppercase (LM hashes are case-insensitive)
    return pot_dict

def process_lm_hash_file(lm_hash_file, pot_dict, export_full):
    """Replace LM hash halves with plaintext equivalents.
    This is used when you crack LM hashes and need to join them back together to make a full password
    The password list should then be run through the case-permutation.py script and used as a password list against
    the NT hashes remaining. 
    
    Expected format of `lm_hash_file` (each line contains a full LM hash - 32 characters long):
        FULL_LM_HASH
    Example:
        299BD128C1101FD6D9D99F2F2B43B62F
        5D41402ABC4B2A76A5E7C9A317E4B403

    If a half-hash is found in the `pot_dict`, it is replaced with its plaintext equivalent.
    If not found, it is replaced with '<HASH_NOT_FOUND>' to indicate missing data.

    Args:
        lm_hash_file (str): Path to a file containing full LM hashes.
        pot_dict (dict): Dictionary mapping LM hash halves to plaintexts.
        export_full (bool): If True, output will include full LM hash along with plaintext.

    Returns:
        list: List of formatted output strings with plaintext replacements.
    """
    output_lines = []
    
    with open(lm_hash_file, 'r', encoding='utf-8') as file:
        for line in file:
            full_lm_hash = line.strip().upper()  # Ensure uppercase
            if len(full_lm_hash) != 32:
                continue  # Skip invalid lines
            
            first_half, second_half = full_lm_hash[:16], full_lm_hash[16:]
            plain_first = pot_dict.get(first_half, <'HASH_NOT_FOUND>')  # Use HASH_NOT_FOUND if not found
            plain_second = pot_dict.get(second_half, '<HASH_NOT_FOUND>')

            if export_full:
                output_lines.append(f"{full_lm_hash}:{plain_first}{plain_second}")
            else:
                output_lines.append(f"{plain_first}{plain_second}")
    
    return output_lines

def main():
    parser = argparse.ArgumentParser(description="Replace LM hash halves with plaintext from a POT file.")
    parser.add_argument(
        "pot_file",
        help="Path to the POT file containing mappings of half LM hashes to plaintext passwords. "
             "Expected format: LM_HASH_HALF:PLAINTEXT (one per line)."
    )
    parser.add_argument(
        "lm_hash_file",
        help="Path to the file containing full LM hashes (32-character hex strings, one per line)."
    )
    parser.add_argument(
        "-o", "--output",
        help="Path to the output file where results will be saved. Default: 'output.txt'.",
        default="output.txt"
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="If set, output will include full LM hash along with the corresponding plaintext. "
             "Otherwise, only the plaintext is output."
    )
    
    args = parser.parse_args()
    
    pot_dict = load_pot_file(args.pot_file)
    results = process_lm_hash_file(args.lm_hash_file, pot_dict, args.full)

    with open(args.output, "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(results) + "\n")
    
    print(f"Processing complete. Results saved to {args.output}")

if __name__ == "__main__":
    main()
