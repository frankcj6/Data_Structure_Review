class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
                new_node.prev = cur
            cur = cur.next

    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.preprend(data)
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                cur.prev = new_node
                new_node.prev = prev
                prev.next = new_node
                new_node.next = cur
            cur = cur.next

    def delete_key(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur.data == key:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def reverse_double(self):
        temp = None
        cur = self.head
        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        if temp:
            self.head = temp.prev

    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur == node:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def remove_duplicates(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt

    def pairs_with_sum(self, sum_val):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append('('+str(p.data)+','+str(q.data)+')')
                q = q.next
            p = p.next
        return pairs


Double_llist = DoublyLinkedList()
Double_llist.append(1)
Double_llist.append(2)
Double_llist.append(3)
Double_llist.prepend(0)

Double_llist.add_after_node(1, 4)
Double_llist.add_before_node(2, 5)
Double_llist.delete_key(4)
Double_llist.print_list()
Double_llist.reverse_double()
Double_llist.print_list()

Double_llist2 = DoublyLinkedList()
Double_llist2.append(1)
Double_llist2.append(2)
Double_llist2.append(3)
Double_llist2.append(3)
Double_llist2.append(4)
Double_llist2.append(4)
Double_llist2.remove_duplicates()
Double_llist2.print_list()
