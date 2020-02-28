dict_alphabets = dict()


def smallestString(weight):
    ascii_value = 66
    final_string = ''
    sum = 1
    dict_alphabets[1] = sum
    for index in range(1, 26):
        sum = (index + 1) * sum + sum
        dict_alphabets[index + 1] = sum
        ascii_value += 1
    print(dict_alphabets)

    while weight != 0:
        largest_alphabet_index = find_largest_alphabet(weight)
        final_string = chr(largest_alphabet_index + 65 - 1) + final_string
        weight = weight - dict_alphabets[largest_alphabet_index]
        print(final_string)


def find_largest_alphabet(weight):
    for key, value in dict_alphabets.items():
        if value > weight:
            return previous
        else:
            previous = key


if __name__ == '__main__':
    smallestString(4)
