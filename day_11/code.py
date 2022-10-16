EXPECTED_OUTPUT_FROM_DESCRIPTION = "abcdffaa"


def process_input(data: list):
    # process input data here
    data = str(data[0])
    return data


def flip(char):
    invalid_chars = 'i', 'o', 'l'
    char = 'a' if char == 'z' else chr(ord(char) + 1)
    if char in invalid_chars:
        char = chr(ord(char) + 1)
    return char


def meets_criteria(pwd):
    increasing_three_letters = False
    non_overlapping_pairs = 0
    for i in range(len(pwd)-2):
        if ord(pwd[i]) == ord(pwd[i+1]) - 1 == ord(pwd[i+2]) - 2:
            increasing_three_letters = True

    i = 0
    while i < len(pwd)-1:
        if pwd[i] == pwd[i+1]:
            non_overlapping_pairs += 1
            i += 2
            continue
        i += 1

    return increasing_three_letters and non_overlapping_pairs >= 2


def part1(input_data):
    input_data = list(input_data)

    hard_stop = "z"*len(input_data)

    while True:
        next_char = flip(input_data[-1])
        input_data[-1] = next_char
        if next_char == 'a':
            for i in range(len(input_data)-2, -1, -1):
                input_data[i] = flip(input_data[i])
                if input_data[i] != 'a':
                    break
        if "".join(input_data) == hard_stop:
            break
        if meets_criteria("".join(input_data)):
            break

    return "".join(input_data)


def part2(input_data):
    return part1(part1(input_data))


if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(__file__), "test_input.txt")) as f:
        data = f.readlines()

    output = part1(process_input(data))
    print(output)
    assert output == EXPECTED_OUTPUT_FROM_DESCRIPTION

    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
        data = f.readlines()

    print(part1(process_input(data)))
    print(part2(process_input(data)))
