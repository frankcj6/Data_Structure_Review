#  solution 1: stack
#  time complexity: O(n)
#  space complexity: O(n)
def is_palindrome_linked_list(head):
    stack = []
    node = head
    while node:
        stack.append(node.val)
        node = node.next
    node = head
    while node:
        if stack[-1] != node.val:
            return False
        stack.pop()
        node = node.next
    return True


#  solution 2: two pointer
#  time complexity: o(n)
#  space complexity: o(1)
def is_palindrome_linked2(head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        rev = rev.next
        slow = slow.next
    return not rev


