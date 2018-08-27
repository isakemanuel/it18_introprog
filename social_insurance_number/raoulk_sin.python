import sys


def remove_non_digits(input_string):
    leftover_digits = ''.join(i for i in input_string if i.isdigit())
    return leftover_digits


def split_string(splittable):
    # Splits a splittable iterable
    split = [int(i) for i in splittable]
    return split


def luhnify(luhn_me):
    luhnified = [a * b for a, b in zip(luhn_me, 5*[2, 1])]
    return luhnified


def digit_splitter(splittable):
    split = [int(d) for d in ''.join(str(x) for x in splittable)]
    return split


def control_length(int_list):
    # Length control & validity control
    if len(int_list) != 10:
        print(len(int_list))
        sys.exit('False length')


def check_validity(checksum):
    if checksum % 10 == 0:
        sys.exit('Success! Correct SIN')
    if checksum % 10 != 0:
        sys.exit('Invalid control value')


if __name__ == '__main__':
    user_input = input('Please enter your SIN (Social Insurance Number): ')
    stripped_sin = remove_non_digits(user_input)
    control_length(stripped_sin)
    split_sin = split_string(stripped_sin)
    luhnified_sin = luhnify(split_sin)
    split_digit_sin = digit_splitter(luhnified_sin)
    check_validity(sum(split_digit_sin))
