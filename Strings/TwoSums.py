'''
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
'''
import time

start_time = time.time()


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_dict = {i: nums[i] for i in range(0, len(nums))}

    length = len(nums)
    result = []
    for i in range(length):
        temp_total = target - nums[i]
        # print ("temp total : ", temp_total)
        if temp_total in nums_dict.values():
            index = ([k for k, v in nums_dict.items() if v == temp_total])
            result.extend(index)

    return result

    #     for j in range(length):
    #         if j == i:
    #             j = i + 1
    #         if i == length:
    #             break
    #         # print("Current Value of i:", i, "       j:", j)
    #         temp_total = nums[i] + nums[j]
    #         # print("total temp: ", temp_total, nums[i], nums[j])q
    #         if temp_total == target:
    #             # print("it matched", i, j)
    #             return [i, j]
    # return [i, j]


if __name__ == '__main__':
    nums = [3,2,4]
    print(twoSum(nums, 6))
    print("--- %s seconds ---" % (time.time() - start_time))
