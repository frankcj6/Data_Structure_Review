#  prepend and append in circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        elif size == 1:
            return self.head
        mid = size // 2
        count = 0
        prev = None
        cur = self.head
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        clist_sub = CircularLinkedList()
        while cur.next != self.head:
            clist_sub.append(cur.data)
            cur = cur.next
        clist_sub.append(cur.data)

        self.print_list()
        print('\n')
        clist_sub.print_list()

    #  Josephus Problem

    def remove_node(self, node):
        if self.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self, step):
        cur = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            self.remove_node(cur)
            print('Currently removing' + str(cur.data))
            cur = cur.next

    def is_circular_linked_list(self, input_list):

        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False

Clist = CircularLinkedList()
Clist.append('A')
Clist.append('B')
Clist.append('C')
Clist.append('D')

Clist.print_list()
Clist.prepend('E')
Clist.print_list()

Clist.remove('B')
Clist.print_list()

Clist.split_list()

Clist1 = CircularLinkedList()
Clist1.append(1)
Clist1.append(2)
Clist1.append(3)
Clist1.append(4)
Clist1.print_list()
Clist1.josephus_circle(2)
Clist1.print_list()

print(Clist1.is_circular_linked_list(Clist1))