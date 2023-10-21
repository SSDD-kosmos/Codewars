class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    if head is None:
        return head
    current = head
    next = current.next
    while next:
        if current.data == next.data:
            current.next = current.next.next
            next = current.next
        else:
            current = next
            next = current.next
    return head
