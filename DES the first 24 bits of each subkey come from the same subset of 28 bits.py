def left_shift(bits, shift_amount):
    return bits[shift_amount:] + bits[:shift_amount]

def generate_keys(initial_key):
    # Define the shift schedule
    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    # Define the bit positions for the first and second subsets
    first_subset_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    second_subset_positions = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

    subkeys = []

    # Generate 16 subkeys
    for i in range(16):
        # Apply left shifts according to the shift schedule
        initial_key = left_shift(initial_key, shift_schedule[i])

        # Select the first 24 bits from the first subset
        first_subset_key = ''.join(initial_key[pos] for pos in first_subset_positions)

        # Select the second 24 bits from the second subset
        second_subset_key = ''.join(initial_key[pos] for pos in second_subset_positions)

        # Combine the two subsets to form the subkey
        subkey = first_subset_key + second_subset_key

        subkeys.append(subkey)

    return subkeys

def main():
    # Example initial key
    initial_key = "0000111100001111000011110000111100001111000011110000111100001111"

    # Generate subkeys
    subkeys = generate_keys(initial_key)

    # Print the generated subkeys
    for i, subkey in enumerate(subkeys):
        print(f"Subkey {i+1}: {subkey}")

if __name__ == "__main__":
    main()
