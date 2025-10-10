class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""Traversal and Simple Manipulation (e.g., finding a node, printing, simple insertion/deletion)"""

def traverse_and_print(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def find_node(head, target):
    current = head
    position = 0
    while current:
        if current.val == target:
            return position
        current = current.next
        position += 1
    return -1  # Not found

"""Fast and Slow Pointer(FLoyd's Tortoise and Hare)"""

def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True # Cycle Detected 
        slow = slow.next
        fast = fast.next.next

    return False # No cycle 

def find_middle(head):
    if not head or not head.next:
        return head
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow # Return the middle node 

"""Pointers with Offset(Nth node from end)"""

def removeNthFromEnd(head, n):
    if not head:
        return None
    
    dummy = ListNode(0) # Dummy node simlifies edge cases (e.g. removing head)
    dummy.next = head
    first = dummy
    second = dummy


    # Advance first pointer 'n' steps ahead
    for _ in range(n + 1): # n + 1 because we want 'second' to be before the node to be removed
        first = first.next

    # Move the pointers until first reaches the end
    while first:
        first = first.next
        second = second.next

    
    # second is now at the node *before* the one to be removed 
    second.next = second.next.next

    return dummy.next # Actual head 

""" Reversing the list"""

def reverse_list(head):
    if not head or not head.next:
        return head
    
    prev = None
    current = head

    while current:
        next_node = current.next #Store the next node
        current.next = prev # Reverse the current Node pointer 
        prev = current # Move prev to current node
        current = next_node # Move current to next node (which was stored in next_temp)
    
    return prev

"""Dummy Node: A dummy node is a false head node added at the beginning of the list. It simplifies the operations,
especially detections or modifications at the head of the list, by providing a consitent previous node for every actual node"""

def delete_duplicates(head):
    if not head or not head.next:
        return head
    
    dummy = ListNode(0, head)
    current = dummy

    while current and current.next and current.next.next:
        if current.next.val == current.next.next.val:
            duplicate_val = current.next.val
            # Skip all nodes with the duplicate value 
            while current.next and current.next.val == duplicate_val:
                current.next = current.next.next
        else:
            current = current.next
    
    return dummy.next # Return new head after Dummy 


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original List:")
    traverse_and_print(head)    
    find_middle(head)
    print(has_cycle)
    find_node(head, 3)
    removeNthFromEnd(head, 2)
    reverse_list(head)
    delete_duplicates(head)
    print("Modified List:")
    traverse_and_print(head)










    


