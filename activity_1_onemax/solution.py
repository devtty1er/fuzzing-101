from enum import Enum
from random import randint, randbytes

INDIVIDUALS_PER_GENERATION = 3
ONEMAX_BITVECTOR_LENGTH = 3

population = []
highest_fitness = -1


def sum_of_bits(data: bytes) -> int:
    """Helper function for your use,
    returns the sum of the bits in data

    For example, see below the sum of
    the single bit that expresses 0x1,
    the two bits that express 0x3,
    and the four bits that express 0xF

    >>> sum_of_bits(b'\x01\x3F')
    7
    """
    sum = 0
    for byte in data:
        for offset in range(0, 7):
            bit = (int(byte) >> offset) & 0x1
            sum += bit
    return sum


class Individual:
    def __init__(self, data: bytes):
        self._data = data
        self.fitness = self.fitness_function()

    def fitness_function(self) -> int:
        """Individual:fitness_function"""
        return sum_of_bits(self._data)

    def as_bit_string(self) -> str:
        s = ""
        for byte in self._data:
            for offset in range(0, 7):
                bit = (int(byte) >> offset) & 0x1
                s += str(bit)
        return s

    def __str__(self):
        return f"Individual {self.as_bit_string()} with fitness {self.fitness}"


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
    # mutation (in this paradigm, there is only one parent)
    parent = pq[0]
    population = []
    for i in range(INDIVIDUALS_PER_GENERATION):
        child = mutate(parent)
        population.append(child)


def main():
    global population
    population = [
        Individual(randbytes(ONEMAX_BITVECTOR_LENGTH + 1))
        for i in range(INDIVIDUALS_PER_GENERATION)
    ]
    while True:
        genetic_algorithm()


if __name__ == "__main__":
    main()
