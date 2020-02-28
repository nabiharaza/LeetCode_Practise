def string_compress(message):
    previous = message[0]
    count = 0
    start = 0
    index = 0
    while index != len(message):
        if previous == message[index]:
            count += 1
        else:
            previous = message[index]
            rest = message[index:]
            message = message[:start + 1]
            count = list(str(count))
            message = message + count
            index = len(message)
            message = message + rest
            count = 1
            start = index
        index += 1
    rest = message[index:]
    message = message[:start + 1]
    count = list(str(count))
    message = message + count
    message = message + rest
    return message


if __name__ == '__main__':
    print(string_compress(["a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c"]))
