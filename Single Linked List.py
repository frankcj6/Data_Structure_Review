# Insertion O(1) Access element O(n)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        new_node = Node(data)
        if not prev_node:
            print('previous node is not in the list.')
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.data.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_position(self, pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def node_swap(self, key1, key2):
        if key1 == key2:
            return
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        if not curr_1 or not curr_2:
            return
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_list(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt
            self.head = prev

    def reverse_list_recursive(self):
        def reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return reverse_recursive(cur, prev)

        self.head = reverse_recursive(cur=self.head, prev=None)

    #  merge two sorted linked list

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

    #  remove duplicates

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_value = dict()

        while cur:
            if cur.data in dup_value:
                prev.next = cur.next
                cur = None
            else:
                dup_value[cur.data] = 1
                prev = cur
            cur = prev.next

    #  Nth- from last node
    #  Method 1: count length
    def n_from_last(self, n):
        total = self.len_iterative()
        cur = self.head
        count = 0
        while cur:
            if total == n:
                print(cur.data)
            total -= 1
            cur = cur.next
        if cur is None:
            return

    #  Method 2: two pointer
    def n_from_last_2(self, n):
        p = self.head
        q = self.head
        count = 0
        while q and count < n:
            q = q.next
            count += 1
        if not q:
            print(str(n) + "is greater than the number of nodes in list.")
        while p and q:
            p = p.next
            q = q.next
        return p.data

    #  count occurrence:
    def count_occurrence_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def count_occurrence_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurrence_recursive(node.next, data)
        else:
            return self.count_occurrence_recursive(node.next, data)

    #  rotate singly linked list

    def rotate_list(self, n):
        p = self.head
        q = self.head
        prev = None
        count = 0
        while p and count < n:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev
        while q:
            prev = q
            q = q.next
        q = prev
        q.next = self.head
        self.head = p.next
        p.next = None

    #  is palindrome(self reflective word)

    #  Method 1: self string check(reverse string)
    def is_palindrome(self):
        s = ''
        cur = self.head
        while cur:
            s += cur.data
            cur = cur.next
        return s == s[::-1]

    #  Method 2: stack
    def is_palindrome_stack(self):
        s = []
        cur = self.head
        while cur:
            s.append(cur.data)
            cur = cur.next

        cur = self.head
        while cur:
            data = s.pop()
            if cur.data != data:
                return False
            cur = cur.next

    #  Method 3:
    def is_palindrome_two_pointer(self):
        p = self.head
        q = self.head
        prev = []
        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i-1]

        count = 1
        while count <= i//2 + 1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True

    #  move tail to head
    def move_tail_to_head(self):
        last = self.head
        second_to_last = None
        while last.next:
            second_to_last = last
            last = last.next
        last.next = self.head
        second_to_last.next = None
        self.head = last

    # sum two list
    def sum_two_list(self, llist):
        p = self.head
        q = llist.head
        sum_list = LinkedList()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_list.append(remainder)
            else:
                carry = 1
                sum_list.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_list.print_list()


llist = LinkedList()
llist.append('A')
llist.append('B')
# llist.print_list()
llist.prepend('C')
# llist.print_list()
llist.insert_after_node(llist.head.next, 'E')
llist.print_list()

# llist.delete_node('B')
# llist.print_list()

# llist.delete_node_at_position(2)
# llist.print_list()

print(llist.len_iterative())
print(llist.len_recursive(llist.head))

llist.node_swap('E', 'A')
llist.print_list()

llist.reverse_list()
llist.print_list()

llist.reverse_list_recursive()
llist.print_list()

llist_1 = LinkedList()
llist_2 = LinkedList()
llist_1.append(1)
llist_1.append(3)
llist_1.append(5)
llist_1.append(7)
llist_2.append(2)
llist_2.append(4)
llist_2.append(6)

llist_1.print_list()
llist_2.print_list()

llist_1.merge_sorted(llist_2)
llist_1.print_list()

llist_3 = LinkedList()
llist_3.append(1)
llist_3.append(2)
llist_3.append(6)
llist_3.append(2)
llist_3.append(3)

llist_3.print_list()

llist_3.remove_duplicates()
llist_3.print_list()

llist_3.n_from_last(2)
print(llist_3.n_from_last_2(2))

llist_4 = LinkedList()
llist_4.append(1)
llist_4.append(2)
llist_4.append(3)
llist_4.append(3)
llist_4.append(4)

llist_4.print_list()
print(llist_4.count_occurrence_iterative(3))
print(llist_4.count_occurrence_recursive(llist_4.head, 3))

llist_4.print_list()
llist_4.rotate_list(3)
llist_4.print_list()
