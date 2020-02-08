def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if (len(s) % 2) != 0:
        return False
    if len(s) == 0:
        return True

    # if s[0] == "]" or s[0] == "}" or s[0] == ")":
    #     return False

    stack_list = []
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            stack_list.append(s[i])
        elif s[i] == ")":
            if stack_list[-1] == "(":
                stack_list.pop(len(stack_list) - 1)
            else:
                return False

        elif s[i] == "]":
            if stack_list[-1] == "[":
                stack_list.index(stack_list[-1])
                stack_list.pop(len(stack_list) - 1)
            else:
                return False
        elif s[i] == "}":
            if stack_list[-1] == "{":
                stack_list.pop(len(stack_list) - 1)
            else:
                return False
    if len(stack_list) != 0:
        return False
    else:
        return True


if __name__ == '__main__':
  print(isValid("(()])}[}[}[]][}}[}{})][[(]({])])}}(])){)((){"))