#include <stdio.h>
#include <stdlib.h>
#include "haystack.h"

#define BUFFER_SIZE 256

int main(int argc, char* argv[]) {
    FILE* file;
    char buffer[BUFFER_SIZE];

    if (argc > 1) {
        file = fopen(argv[1], "r");
        if (file == NULL) {
            fprintf(stderr, "Unable to open file: %s\n", argv[1]);
            return 1;
        }
    } else {
        file = stdin;
    }

    if (fgets(buffer, sizeof(buffer), file) == NULL) {
        fprintf(stderr, "Unable to read from %s\n", argc > 1 ? argv[1] : "stdin");
        return 1;
    }

    if (argc > 1) {
        fclose(file);
    }

    check(buffer);
    return 0;
}