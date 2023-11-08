#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Compile with gcc -O3 -march=native -o case-permutation case-permutation.c
// Note that if you stream output to the console, it's extremely slow. Best to write into a file 
// Run with: ./case-permutation example outputfile.txt

#define MAX_LENGTH 24

void printPermutations(FILE *stream, char *word, int index, int length) {
    if (index == length) { // When index reaches the word length, print the permutation
        fprintf(stream, "%s\n", word);
        return;
    }

    // Save the current character
    char current = word[index];

    // Recursively generate permutations with lowercase current letter
    word[index] = tolower(current);
    printPermutations(stream, word, index + 1, length);

    // Recursively generate permutations with uppercase current letter
    // Only if it's different from the lowercase character
    if (tolower(current) != toupper(current)) {
        word[index] = toupper(current);
        printPermutations(stream, word, index + 1, length);
    }

    // Restore the character
    word[index] = current;
}

int main(int argc, char *argv[]) {
    char word[MAX_LENGTH + 1]; // +1 for the null terminator
    FILE *output_stream = stdout; // Default to stdout

    if (argc >= 2) {
        strncpy(word, argv[1], MAX_LENGTH);
        word[MAX_LENGTH] = '\0'; // Ensure null-termination
    } else {
        printf("Please enter the word (up to %d characters): ", MAX_LENGTH);
        if (fgets(word, sizeof(word), stdin) == NULL) {
            perror("Error reading input");
            return EXIT_FAILURE;
        }
        word[strcspn(word, "\n")] = 0; // Remove newline character
    }

    int length = strlen(word);

    char *output_file = argc >= 3 ? argv[2] : NULL;

    if (output_file) {
        output_stream = fopen(output_file, "w");
        if (!output_stream) {
            perror("Error opening file");
            return EXIT_FAILURE;
        }
    }

    // Generate and print/write permutations
    printPermutations(output_stream, word, 0, length);

    if (output_stream != stdout) {
        fclose(output_stream);
        printf("Permutations written to %s\n", output_file);
    }

    return EXIT_SUCCESS;
}

