def validSubarrays(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    mega_list = []
    for numbers in nums:
        mega_list.append(numbers)
    print(mega_list)

    index = 0

    while index != (len(mega_list) - 1):
        next_list = mega_list[index + 1]
        if type(next_list) == int and type(mega_list[index]) == int:
            if mega_list[index] < next_list:
                temp = []
                temp.append(mega_list[index])
                temp.append(next_list)
                mega_list.append(temp)
        elif type(next_list) == list and type(mega_list[index]) == int:
            print(mega_list[index])
            print(next_list[0])
            if mega_list[index] < next_list[0]:
                temp = []
                temp.append(mega_list[index])
                temp.append(next_list)
                mega_list.append(temp)
        else:
            print(mega_list[index])
            print(next_list[0])
            if mega_list[index][0] < next_list[0]:
                temp = mega_list[index] + next_list
                mega_list.append(temp)
        index += 1

    print(mega_list)


if __name__ == '__main__':
    print(validSubarrays([1, 4, 2, 5, 3]))
    # print(validSubarrays([3, 2, 1]))
    # print(validSubarrays([2, 2, 2]))
