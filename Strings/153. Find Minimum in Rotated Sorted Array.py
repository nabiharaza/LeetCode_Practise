def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []:
        return 0
    min_number = nums[0]

    for i in range(len(nums) - 1):
        if nums[i + 1] < nums[i]:
            return nums[i + 1]
    return min_number


if __name__ == '__main__':
    print(findMin([4, 5, 6, 7, 0, 1, 2]))
    print(findMin([3, 4, 5, 1, 2]))
    print(findMin([1]))
    print(findMin([1, 2, 3]))
    print(findMin([]))

# Same code can be used for the hard question becuase it deals with Duplicates
