import argparse

def load_pot_file(pot_file):
    """
    Load the POT file into a dictionary mapping NT hashes to plaintext passwords.

    Expected formats (each line in the file):
      - John format: $NT$<32 Character NT Hash>:<password>
      - Hashcat format: <32 Character NT Hash>:<password>

    Returns:
        dict: A dictionary where keys are NT hashes (uppercase) and values are plaintext passwords.
    """
    pot_dict = {}
    with open(pot_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            # Remove the $NT$ prefix if present (John format)
            if line.startswith("$NT$"):
                line = line[len("$NT$"):]
            parts = line.split(":", 1)
            if len(parts) == 2:
                nt_hash, plaintext = parts
                nt_hash = nt_hash.upper()
                if len(nt_hash) == 32:
                    pot_dict[nt_hash] = plaintext
    return pot_dict

def process_hash_file(hash_file, pot_dict, export_full):
    """
    Replace NT hashes with their plaintext equivalents.

    The hash file can be in one of two formats:
      - dcsync file: value:value:LM:<32 Character NT Hash>:::
      - NT file: <32 Character NT Hash>

    For a dcsync file, the script replaces the fourth field (index 3) with the plaintext
    (if found in the pot file). For an NT file, it simply looks up the hash.
    
    Args:
        hash_file (str): Path to the file containing NT hashes.
        pot_dict (dict): Dictionary mapping NT hashes (uppercase) to plaintext passwords.
        export_full (bool): If True, output the full line with the NT hash substituted by plaintext.
                            Otherwise, only output the plaintext.
                            
    Returns:
        list: List of formatted output strings with substituted plaintext.
    """
    output_lines = []
    
    with open(hash_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            # Check if the line is in dcsync file format (colon separated with at least 4 fields and the 3rd field equals "LM")
            fields = line.split(':')
            if len(fields) >= 4 and fields[2].upper() == "LM":
                nt_hash = fields[3].upper()
                if len(nt_hash) != 32:
                    continue  # Skip if not a valid NT hash
                plaintext = pot_dict.get(nt_hash, "<HASH_NOT_FOUND>")
                if export_full:
                    # Replace the NT hash in its original location (fourth field) with the plaintext
                    fields[3] = plaintext
                    output_lines.append(":".join(fields))
                else:
                    output_lines.append(plaintext)
            else:
                # Otherwise assume the line is a simple NT file format (just a 32-character hash)
                nt_hash = line.upper()
                if len(nt_hash) != 32:
                    continue  # Skip invalid lines
                plaintext = pot_dict.get(nt_hash, "<HASH_NOT_FOUND>")
                if export_full:
                    output_lines.append(f"{nt_hash}:{plaintext}")
                else:
                    output_lines.append(plaintext)
    
    return output_lines

def main():
    parser = argparse.ArgumentParser(
        description="Replace NT hashes with plaintext from a POT file. "
                    "POT file formats supported: '$NT$<32 NT hash>:<password>' (John) and '<32 NT hash>:<password>' (Hashcat). "
                    "Hash file formats supported: dcsync file (value:value:LM:<32 NT hash>:::) or a simple NT file (<32 NT hash>)."
    )
    parser.add_argument(
        "pot_file",
        help="Path to the POT file containing NT hash to plaintext mappings."
    )
    parser.add_argument(
        "hash_file",
        help="Path to the file containing NT hashes in dcsync or NT file format."
    )
    parser.add_argument(
        "-o", "--output",
        help="Path to the output file where results will be saved. Default: 'output.txt'.",
        default="output.txt"
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="If set, output will include full original line structure with the NT hash replaced by the plaintext. "
             "Otherwise, only the plaintext is output."
    )
    
    args = parser.parse_args()
    
    pot_dict = load_pot_file(args.pot_file)
    results = process_hash_file(args.hash_file, pot_dict, args.full)

    with open(args.output, "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(results) + "\n")
    
    print(f"Processing complete. Results saved to {args.output}")

if __name__ == "__main__":
    main()
