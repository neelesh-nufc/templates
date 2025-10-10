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
    """Finds the middle node of a linked list.
    If the list has an even number of nodes, it returns the second of the two middle nodes.
    """
    if not head or not head.next:
        return head
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow # Return the middle node itself

"""Pointers with Offset(Nth node from end)"""

def removeNthFromEnd(head, n):
    if not head:
        return None
    
    dummy = ListNode(0) # Dummy node simlifies edge cases (e.g. removing head)
    dummy.next = head
    first = dummy
    second = dummy


    # Advance first pointer 'n' steps ahead
    for _ in range(n+1): # n because we want 'second' to be before the node to be removed
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
    """Reverses a linked list iteratively and returns the new head."""
    if not head or not head.next:
        return head
    
    prev = None
    current = head

    while current:
        next_node = current.next # Store the next node
        current.next = prev # Reverse the current Node pointer 
        prev = current # Move prev to current node
        current = next_node # Move current to the original next node
    
    return prev

"""Dummy Node: A dummy node is a false head node added at the beginning of the list. It simplifies the operations,
especially detections or modifications at the head of the list, by providing a consitent previous node for every actual node"""

def delete_duplicates(head):
    """Given the head of a sorted linked list, delete duplicates such that each element appears only once.
    Example: 1->1->2->3->3 becomes 1->2->3
    """
    if not head:
        return None
    
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next # Skip the duplicate
        else:
            current = current.next # Move to the next distinct node
    
    return head

def delete_all_duplicates(head):
    """Given the head of a sorted linked list, delete ALL nodes that have duplicate numbers,
    leaving only distinct numbers from the original list. Return the linked list sorted as well.
    Example: 1->2->3->3->4->4->5 becomes 1->2->5
    Example: 1->1->1->2->3 becomes 2->3
    """
    if not head or not head.next:
        return head
    
    dummy = ListNode(0, head)
    prev = dummy # prev will point to the last node of the valid, non-duplicate list

    while head:
        if head.next and head.val == head.next.val:
            # Skip all nodes with this duplicate value
            while head.next and head.val == head.next.val:
                head = head.next
            prev.next = head.next # Skip the entire duplicate sequence
        else:
            prev = prev.next
        head = head.next
    
    return dummy.next # Return new head after Dummy


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original List:")
    traverse_and_print(head)   
    print("find middle:") 
    middle_node = find_middle(head)
    print(middle_node.val if middle_node else "None")
    print("has cycle:")
    print(has_cycle(head))
    print("find node:") 
    print(find_node(head, 3))


    # The functions that modify the list structure return the new head.
    # It's important to capture this new head to reflect the changes.
    print("\nList after removing 2nd from end (node 4):")
    head = removeNthFromEnd(head, 2)
    traverse_and_print(head)


    print("\nList after reverse:")
    head = reverse_list(head)
    traverse_and_print(head)
    
    # Let's test the two different duplicate deletion functions.
    print("\n--- Testing Duplicate Deletion ---")
    dup_head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3, ListNode(4)))))))
    
    print("\nOriginal list with duplicates:")
    traverse_and_print(dup_head)

    # Test the version that keeps one of each duplicate element (your expected output)
    # We need to create a new list or reset it, as the functions modify the list in-place.
    dup_head_for_adj = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3, ListNode(4)))))))
    dup_head_for_adj = delete_duplicates(dup_head_for_adj)
    print("\nAfter delete_duplicates (keeps one of each):")
    traverse_and_print(dup_head_for_adj)

    # Test the version that removes ALL nodes that are part of a duplicate sequence
    dup_head = delete_all_duplicates(dup_head)
    print("\nAfter delete_all_duplicates (removes all duplicate nodes):")
    traverse_and_print(dup_head)
