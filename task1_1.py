import random


def legitimate_channel(input_word):
    possible_errors = ["0000000", "0000001", "0000010",
                       "0000100", "0001000", "0010000", "0100000", "1000000"]
    output_words = []

    for error in possible_errors:
        output_word = ''.join(str(int(bit_a) ^ int(bit_b))
                              for bit_a, bit_b in zip(input_word, error))
        output_words.append(output_word)

    return output_words


def eavesdropper_channel(input_word):
    output_words = []

    # Randomly choose how many errors to introduce (up to 3)
    num_errors = random.randint(0, 3)

    for _ in range(num_errors):
        # Randomly choose the position of the error
        error_position = random.randint(0, 6)

        # Flip the bit at the chosen position
        input_word = input_word[:error_position] + str(
            int(not int(input_word[error_position]))) + input_word[error_position+1:]

    output_words.append(input_word)

    return output_words


def is_valid_7bit_word(word):
    if len(word) == 7 and all(bit in '01' for bit in word):
        return True
    else:
        return False


while True:
    input_word = input("Enter a 7-bit word: ")
    if is_valid_7bit_word(input_word):
        break
    else:
        print("Invalid input. Please enter a 7-bit word consisting of 0s and 1s.")

legitimate_output = legitimate_channel(input_word)
print(f"Legitimate channel output for input {input_word}: {legitimate_output}")

eavesdropper_output = eavesdropper_channel(input_word)
print(
    f"Eavesdropper channel output for input {input_word}: {eavesdropper_output}")
