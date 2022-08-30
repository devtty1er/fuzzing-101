#include <stdio.h>
#include <stdlib.h>
#include "haystack.h"

#define BUFFER_SIZE 256

int main(int argc, char* argv[]) {
    char buffer[BUFFER_SIZE] = "foobar";
    check(buffer);
    return 0;
}