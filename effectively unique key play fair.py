import math

def calculate_possible_keys():
    # Without considering equivalent keys
    keys_without_equivalent = math.factorial(25) // math.factorial(25 - 5)

    # Taking into account equivalent keys
    # We need to divide the total number of keys by the number of equivalent keys
    # The number of equivalent keys depends on the symmetrical properties of the Playfair matrix
    # It's hard to calculate the exact number of equivalent keys, so we'll approximate
    # A conservative estimate is to consider each key as equivalent to all its rotations and reflections
    # There are 8 symmetrical transformations (4 rotations and 4 reflections)
    number_of_equivalent_transformations = 8
    keys_with_equivalent = keys_without_equivalent // number_of_equivalent_transformations

    return keys_without_equivalent, keys_with_equivalent

def main():
    keys_without_equivalent, keys_with_equivalent = calculate_possible_keys()
    print("Number of possible keys without considering equivalent keys:", keys_without_equivalent)
    print("Number of effectively unique keys, taking into account equivalent keys:", keys_with_equivalent)

if __name__ == "__main__":
    main()
