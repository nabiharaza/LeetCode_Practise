def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    dict = {}
    count = 1
    max_count = 0
    for letter in list(s):
        key, value = letter, count
        if key not in dict:
            dict[key] = [value]
        else:
            dict[key].append(value)
    nonrepeated_list = (list(dict))
    all_substring_list = []

    s = list(s)

    for i in s:
        if i in all_substring_list:
            all_substring_list = all_substring_list[all_substring_list.index(i) + 1:]

        all_substring_list.append(i)
        max_count = max(max_count, len(all_substring_list))

    return max_count


if __name__ == '__main__':
    # print(lengthOfLongestSubstring('abcabcbb'))

    print(lengthOfLongestSubstring('pwwkew'))
    print(lengthOfLongestSubstring('bbbbb'))
    print(lengthOfLongestSubstring('abcbabcbwyztsf'))
