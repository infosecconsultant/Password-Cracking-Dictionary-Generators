import argparse

def load_pot_file(pot_file):
    """Load the POT file into a dictionary mapping LM hash halves to plaintexts."""
    pot_dict = {}
    with open(pot_file, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(':', 1)
            if len(parts) == 2:
                lm_half, plaintext = parts
                pot_dict[lm_half.upper()] = plaintext  # Store in uppercase (LM hashes are case-insensitive)
    return pot_dict

def process_lm_hash_file(lm_hash_file, pot_dict, export_full):
    """Replace LM hash halves with plaintext equivalents."""
    output_lines = []
    
    with open(lm_hash_file, 'r', encoding='utf-8') as file:
        for line in file:
            full_lm_hash = line.strip().upper()  # Ensure uppercase
            if len(full_lm_hash) != 32:
                continue  # Skip invalid lines
            
            first_half, second_half = full_lm_hash[:16], full_lm_hash[16:]
            plain_first = pot_dict.get(first_half, '<NOT_CRACKED_YET>' * 7)  # Use '<NOT_CRACKED_YET>' if not found
            plain_second = pot_dict.get(second_half, '<NOT_CRACKED_YET>' * 7)

            if export_full:
                output_lines.append(f"{full_lm_hash}:{plain_first}{plain_second}")
            else:
                output_lines.append(f"{plain_first}{plain_second}")
    
    return output_lines

def main():
    parser = argparse.ArgumentParser(description="Replace LM hash halves with plaintext from a POT file.")
    parser.add_argument("pot_file", help="Path to the POT file (half hashes to plaintext mappings).")
    parser.add_argument("lm_hash_file", help="Path to the full LM hashes file.")
    parser.add_argument("-o", "--output", help="Output file to save results.", default="output.txt")
    parser.add_argument("--full", action="store_true", help="Export full LM hash with full plaintext (default: plaintext only).")
    
    args = parser.parse_args()
    
    pot_dict = load_pot_file(args.pot_file)
    results = process_lm_hash_file(args.lm_hash_file, pot_dict, args.full)

    with open(args.output, "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(results) + "\n")
    
    print(f"Processing complete. Results saved to {args.output}")

if __name__ == "__main__":
    main()
