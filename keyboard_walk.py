import argparse

def get_adjacent_keys(key, keyboard):
    """Find all adjacent keys for a given key."""
    adjacent = []
    for i in range(len(keyboard)):
        for j in range(len(keyboard[i])):
            if keyboard[i][j] == key:
                # Check all adjacent positions
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if 0 <= i + x < len(keyboard) and 0 <= j + y < len(keyboard[i + x]) and (x != 0 or y != 0):
                            adjacent.append(keyboard[i + x][j + y])
    return adjacent

def generate_walks(start_key, length, keyboard, path="", walks=None):
    """Recursively generate all walks of a given length starting from a specific key."""
    if walks is None:
        walks = []

    if length == 0:
        walks.append(path)
        return walks

    for adj_key in get_adjacent_keys(start_key, keyboard):
        generate_walks(adj_key, length - 1, keyboard, path + adj_key, walks)

    return walks

def keyboard_walks(length, layout):
    """Generate all keyboard walks of a specified length for a given layout."""
    layouts = {
        "qwerty": [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\''],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
        ],
        "qwertyshifted": [
            ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+'],
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\''],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
        ],
        "qwertyshifted1": [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
            ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+'],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\''],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
        ],
        "qwertyshifted2": [
            ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+'],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\''],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
        ],
        "dvorak": [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '[', ']'],
            ['\'', ',', '.', 'p', 'y', 'f', 'g', 'c', 'r', 'l', '/', '=', '\\'],
            ['a', 'o', 'e', 'u', 'i', 'd', 'h', 't', 'n', 's', '-'],
            [';', 'q', 'j', 'k', 'x', 'b', 'm', 'w', 'v', 'z'],
        ],
        "azerty": [
            ['²', '&', 'é', '"', '\'', '(', '-', 'è', '_', 'ç', 'à', ')', '=', '\\'],
            ['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '^', '$'],
            ['q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'ù', '*'],
            ['<', 'w', 'x', 'c', 'v', 'b', 'n', ',', ';', ':', '!'],
        ]
    }

    keyboard = layouts[layout]

    all_walks = []
    for row in keyboard:
        for key in row:
            all_walks.extend(generate_walks(key, length - 1, keyboard, key))

    return all_walks

def main():
    parser = argparse.ArgumentParser(description="Generate keyboard walks.")
    parser.add_argument("-l", "--length", type=int, help="Length of the walks", required=True)
    parser.add_argument("-o", "--output", type=str, help="Output file name", required=True)
    parser.add_argument("-k", "--layout", type=str, choices=["qwerty", "qwertyshifted", "qwertyshifted1", "qwertyshifted2", "dvorak", "azerty"], default="qwerty", help="Keyboard layout")

    args = parser.parse_args()

    walks = keyboard_walks(args.length, args.layout)
    total_walks = len(walks)

    print(f"Total walks to be generated: {total_walks}")
    confirm = input("Do you want to proceed with generation? (yes/no): ")
    if confirm.lower() == 'yes':
        with open(args.output, 'w') as file:
            for walk in walks:
                file.write(walk + '\n')
        print(f"Walks written to {args.output}")
    else:
        print("Generation cancelled.")

if __name__ == "__main__":
    main()
