# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def removeKFromList(l, k):
    if l == None: return None
    ret = []
    while l:
        if l.value == k:
            if l.next == None:
                l.next = None
                return ret
            else: l = l.next
        else:
            ret.append(l.value)
            l = l.next
    return ret


temp = ListNode(5)
temp2 = ListNode(6)
temp.next = temp2
print(removeKFromList(temp, 5))
