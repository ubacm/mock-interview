#/usr/bin/python3

# Question here
# Implement a function to find the center element in a linked list
#
# Input: Linked list node (head)
# Output: Linked list node (center)

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

def solution1(head):
    if head is None:
        return None
    curNode = head
    midNode = head
    count = 0
    while curNode.next:
        count += 1 
        curNode = curNode.next
        if count%2 == 0:
            midNode = midNode.next

    return midNode
        
if __name__ == "__main__":
    head = Node(1)
    curNode = head
    for idx in range(2,40): # values range from 1 to 39, result will be 20
        curNode.next = Node(idx)
        curNode = curNode.next

    result = solution1(head)
    if result is not None:
        print(result.val)
    else:
        print(result)
