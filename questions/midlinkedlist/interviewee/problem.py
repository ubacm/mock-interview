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



if __name__ == "__main__":
    head = Node(1)
    curNode = head
    for idx in range(2,40): # values range from 1 to 39, result will be 20
        curNode.next = Node(idx)
        curNode = curNode.next
