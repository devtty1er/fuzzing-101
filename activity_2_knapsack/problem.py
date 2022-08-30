from enum import Enum
from random import randint
import argparse
from typing import NamedTuple
from time import time
from pathlib import Path

# Download classic-01-knapsack-testcases.zip from
# https://www.hackerrank.com/rest/contests/srin-aadc03/challenges/classic-01-knapsack/download_testcases

INDIVIDUALS_PER_GENERATION = 3

population = []
starting_individual = None
highest_fitness = -1
items = []
capacity = None


class Individual:
    def __init__(self, data: bytes):
        self._data = data
        self.fitness = self._fitness_function()

    def _fitness_function(self):
        global items
        total_value = 0
        total_weight = 0
        for i, byte in enumerate(self._data):
            for offset in range(0, 7):
                bit = (int(byte) >> offset) & 0x1
                if bit:
                    try:
                        item = items[i * 8 + offset]
                        total_value += item.value
                        total_weight += item.weight
                    except IndexError:
                        return -1
        if total_weight > capacity:
            return -1
        return total_value

    def __eq__(self, other):
        return self._data == other._data

    def __str__(self):
        return f"Individual {self._data} with fitness {self.fitness}"


class ObjectiveFunction(Enum):
    MINIMIZE = 1
    MAXIMIZE = 2


class SimplePriorityQueue:
    """This is a terrible priority queue implementation, which
    re-sorts on insertion, but insertion is the edge case and
    this is sufficient for demonstration.

    The fittest individual is always at index 0
    """

    def __init__(self, objective_function: ObjectiveFunction):
        self._objective_function = objective_function
        self._pq = []

    def add(self, entry: Individual):
        self._pq.append(entry)
        self._pq.sort(
            key=lambda e: e.fitness,
            reverse=(self._objective_function == ObjectiveFunction.MAXIMIZE),
        )

    def __len__(self):
        return len(self._pq)

    def __getitem__(self, key):
        return self._pq[key]


def mutate(parent: Individual) -> Individual:
    """Basic xor mutator"""
    data = bytearray(parent._data)  # bytes are immutable
    random_bit = randint(0, (len(data) * 8) - 1)
    data[random_bit >> 3] ^= 0x1 << (random_bit % 8)
    child = Individual(bytes(data))
    return child


pq = SimplePriorityQueue(ObjectiveFunction.MAXIMIZE)


def genetic_algorithm():
    global population, pq, highest_fitness
    # evaluation
    for individual in population:
        fitness = individual.fitness
        # selection
        if fitness > highest_fitness:
            print(individual)
            highest_fitness = fitness
            pq.add(individual)
    # TODO: Activity 2, overcome local optima
    # mutation
    parent = pq[0]
    population = []
    for i in range(INDIVIDUALS_PER_GENERATION):
        child = mutate(parent)
        population.append(child)


class Item(NamedTuple):
    weight: int
    value: int


def parse_hackerrank_qa(input_file, output_file) -> tuple:
    """Parse hackerrank format, returning the solution from the output file and
    a list of Item from the input_file
    """
    global capacity
    with open(output_file, "r") as f:
        solution = int(f.read())
    _items = []
    with open(input_file, "r") as f:
        # the input format is kind of silly...
        # AFAIK the first line is always 1
        # the second line is: <knapsack capacity> <number of lines below>
        # the following lines are: <weight> <value>
        for i, l in enumerate(f.readlines()):
            if i == 0:
                continue  # the first line is always 1?
            elif i == 1:
                _capacity, _lines = tuple(l.split())
                capacity = int(_capacity)
                continue
            _weight, _value = tuple(l.split())
            _items.append(Item(int(_weight), int(_value)))
    return (solution, _items)


def main(input_file: Path, output_file: Path):
    global items, starting_individual, capacity, population
    solution, items = parse_hackerrank_qa(input_file, output_file)
    # how many bytes are needed to express taken/not taken as bits
    byte_count = int(len(items) / 8)
    if len(items) % 8:
        byte_count += 1
    # start by "taking" nothing
    starting_individual = Individual(b"\x00" * byte_count)
    population = [starting_individual]
    t0 = time()
    while highest_fitness != solution:
        genetic_algorithm()
    tf = time()
    print(f"Found the optimal solution in {tf - t0}!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path1", type=Path)
    parser.add_argument("path2", type=Path)
    args = parser.parse_args()
    main(args.path1, args.path2)
