def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    dict = {}
    duplicates_list = []
    count = 0
    for numbers in nums:
        key, value = numbers, count
        count = 1
        if key not in dict:
            dict[key] = count
        else:
            count = dict.get(key)
            count = count + 1
            dict[key] = count
    print(dict)

    for key in dict:
        if dict.get(key) > 1:
            duplicates_list.append(key)

    print(duplicates_list)

if __name__ == '__main__':
    findDuplicates([4,3, 2, 7, 8, 2, 3, 1])
