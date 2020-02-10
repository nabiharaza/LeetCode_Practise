def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    duplicate_nums = nums.copy()  # list to list copy is a shallow copy and modifies the actual contents
    duplicate_nums.sort()
    for i in range(len(duplicate_nums)):
        if duplicate_nums[i] == target:
            print(i)
            return (nums.index(duplicate_nums[i]))

    return -1


if __name__ == '__main__':
    print(search([4, 5, 6, 7, 0, 1, 2], 4))
