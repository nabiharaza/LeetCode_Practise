# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# l1 = [3,40,5]
# l2 = [33,55,66]

[1, 2, 4]
[1, 3, 4]


def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    merged_list = []
    for i in l1:
        if l1[i] < l2[i]:
            merged_list.append(l1[i])
        elif l2[i] > l1[i]:
            merged_list.append(l2[i])
    else:
        merged_list.append(l1[i])
        merged_list.append(l2[i])

    if len(merged_list) < len(l1) + len(l2):
        for i in range(len(l2)):
            merged_list.append(l2[i])

    print (merged_list)

