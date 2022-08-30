# afl

Activity 3 -- "AFL" is meant to serve as an introduction to understanding (1) how to use AFL and (2) how AFL implements different GA components.

For the purposes of this activity, we use `afl-gcc`, which is not the best afl-compiler to use; however, it is the easiest to explain and observe in isolation.

Run `docker-compose up` to create the `main_static` executable using AFL.

## Activity 1

Compile and fuzz `haystack.c` (main static variant) using AFL. Reference AFL's README.

## Activity 2

Disassemble and reverse engineer the `__afl_maybe_log` function (instrumentation compiled into `haystack`).

## Challenge

Re-implement `evaluate()` and `fitness_function()` in `python_model_fuzzer.py` to support the `afl-gcc`-compiled `haystack` (main static variant). You can reference `afl-fuzz` source code, the instrumentation, and/or disassembled versions of `afl-fuzz` and `haystack`.

## Question

What are the differences between fuzzing `haystack` and fuzzing `python_model.py`? These represent two extremes on a scales of model fidelity (original vs. re-written), speed optimizations (C w/ forkserver vs. Python), and instrumentation complexity (bitmap vs. coverage counter). How would these differences affect real-world targets?
