import math
import os
import random
import re
import sys


#
# Complete the 'deviceNamesSystem' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY devicenames as parameter.
#
def deviceNamesSystem(devicenames):
    dict = {}
    count = 0
    for devices_index in range(len(devicenames)):
        key, value = devicenames[devices_index], count
        count = 0
        if key not in dict:
            dict[key] = count
        else:
            count = dict.get(key)
            count = count + 1
            dict[key] = count
            if count > 0:
                devicenames[devices_index] = devicenames[devices_index] + str(count)
                print(devicenames[devices_index])
    print(dict)
    return devicenames


if __name__ == '__main__':
    print(deviceNamesSystem(['switch', 'tv', 'switch', 'tv', 'tv', 'tv']))
