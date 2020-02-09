def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    sentence_list = s.split()
    if sentence_list == []:
        return 0
    else:
        return len(sentence_list[-1])


if __name__ == '__main__':
    print(lengthOfLastWord("Nabiha Raza"))
    print(lengthOfLastWord("Snakes"))
    print(lengthOfLastWord(""))
