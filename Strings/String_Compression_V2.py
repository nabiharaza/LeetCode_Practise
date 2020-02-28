def compress(orginial_list):
    compressed_list = []
    mark_X = True
    if orginial_list == []:
        return 0
    if len(orginial_list) == 1:
        return 1

    if len(orginial_list) > 1:
        count = 1
        for i in range(len(orginial_list) - 1):
            begin_pointer = i

            if orginial_list[i] == orginial_list[i + 1]:
                count = count + 1
                if count > 2:
                    orginial_list[i + 1] = 'X'
                print("count in greater than 2,", count)
                print(orginial_list)

            else:
                if count > 1:
                    orginial_list[begin_pointer + 1] = count
                    count = 1
                    # remaining_list = orginial_list[begin_pointer + 1:]


if __name__ == '__main__':
    print(compress(["a", "a", "b", "b", "c", "c", "c"]))
    # print(compress(["a"]))
    # print(compress(["a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
    # print(compress([["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    #                 ]))
