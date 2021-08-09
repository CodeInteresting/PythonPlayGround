class LinkNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# Insert From Tail
def CreateLinkList(items=None):
    dummyHead = LinkNode(None)
    if (items is not None):
        tail = dummyHead  # Insert From Tail
        for item in list(items):
            tail.next = LinkNode(item)
            tail = tail.next
    return dummyHead


# Insert From Head
def CreateLinkList2(items=None):
    dummyHead = LinkNode(None)
    if (items is not None):
        for item in list(items):
            oldNext = dummyHead.next
            dummyHead.next = LinkNode(item)
            dummyHead.next.next = oldNext
    return dummyHead


# Without Dummy Head | insert from head
def CreateLinkList3(items=None):
    pHead = None
    if (items is not None):
        ls = list(items)
        if len(ls) > 0:
            pHead = LinkNode(ls[0])
            for item in ls[1:]:
                oldHead = pHead
                pHead = LinkNode(item)
                pHead.next = oldHead
    return pHead


# Without Dummy Head | insert from tail
def CreateLinkList4(items=None):
    pHead = None
    pTail = None
    if (items is not None):
        ls = list(items)
        if len(ls) > 0:
            pTail = pHead = LinkNode(ls[0])
            for item in ls[1:]:
                pTail.next = LinkNode(item)
                pTail = pTail.next
    return pHead


# Print when dummy head exists
def PrintLinkList(linkList):
    p = linkList.next
    while p:
        print(p.value)
        p = p.next


# Print without dummy head
def PrintLinkList2(linkList):
    p = linkList
    while p:
        print(p.value)
        p = p.next


llist = CreateLinkList4([23, 33, 45, 78])
PrintLinkList2(llist)
