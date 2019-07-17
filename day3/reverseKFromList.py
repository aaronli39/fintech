# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def reverseNodesInKGroups(l, k):
        # len1 = 0
        # while l:
        #     len1 += 1
        #     l = l.next
        # for i in range(len1 // k):
    if not l or not l.next:
        return None
    
    val = l

    # reversing linked list
    def rev(head, k):
        if head == None or head.next == None:
            return None
        
        ret = None
        while head:
            temp = head
            head = temp.next
            temp.next = ret
            ret = temp
        return ret

    counter = 0
    while counter < k and val:
        val = val.

    ans = rev(l)
    ret = []
    while ans:
        ret.append(ans.value)
        ans = ans.next
    print(ret)

thing = ListNode(5)
thing2 = ListNode(6)
thing3 = ListNode(1)

thing3.next = thing 
thing.next = thing2
thing2.next = None
print(reverseNodesInKGroups(thing3, 2))