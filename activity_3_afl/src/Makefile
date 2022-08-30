CC := $(CC)
CFLAGS := -Wall -Werror

all: libhaystack.so main_dynamic main_static main_noinput

libhaystack.so: haystack.c haystack.h
	$(CC) $(CFLAGS) -shared -fPIC -o $@ $<

main_dynamic: main.c libhaystack.so
	$(CC) $(CFLAGS) -o $@ $< -L. -lhaystack

main_static: main.c haystack.c haystack.h
	$(CC) $(CFLAGS) -static haystack.c -o $@ $<

main_noinput: main_noinput.c haystack.c haystack.h
	$(CC) $(CFLAGS) -static haystack.c -o $@ $<

clean:
	rm -f libhaystack.so main_dynamic main_static main_noinput
