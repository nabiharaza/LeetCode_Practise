import itertools


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    dict = {}
    start = 0
    stop = 3

    number_list = [2, 3, 4, 5, 6, 7, 8, 9]
    mega_list = []
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

    for number in number_list:
        value = abc[start:stop]
        key, value = number, value
        if key not in dict:
            if key == 9 or key == 7:
                value = abc[start:stop + 1]
                dict[key] = abc[start:stop + 1]
                # print(key, ":  ", value)

            elif key == 8:
                stop = stop + 1
                start = start + 1
                value = abc[start:stop]
                dict[key] = abc[start:stop]
                # print(key, ":  ", value)
            else:
                # print(key, ":  ", value)
                dict[key] = value
            start = start + 3
            stop = stop + 3

    digits_list = list(str(digits))

    for i in range(0, len(digits_list)):
        digits_list[i] = int(digits_list[i])

    for key in digits_list:
        if key in dict.keys():
            mega_list.append(dict[key])

        else:
            print("Not present")
    print(mega_list)

    res = list(itertools.product(*mega_list))
    print((str(res)))

    res = [' '.join(tups) for tups in res]
    return ((str(res)))


if __name__ == '__main__':
    letterCombinations(23)
