#include <stdlib.h>
#include <stdint.h>
#include <signal.h>
#include "haystack.h"

void check(char *buf) {
    if (buf[0] != 'n') {
        exit(1);
    }
    else if (buf[1] != 'e') {
        exit(1);
    }
    else if (buf[2] != 'e') {
        exit(1);
    }
    else if (buf[3] != 'd') {
        exit(1);
    }
    else if (buf[4] != 'l') {
        exit(1);
    }
    else if (buf[5] != 'e') {
        exit(1);
    }
    raise(SIGSEGV);
}
