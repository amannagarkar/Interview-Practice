from src.LinkedList.Node import Node


class LinkedList:
    def __init__(self, head=None):
        self.curr = None
        self.head = head
        self.length = 0

    def add_node(self, value):
        node = Node(value)
        self.length += 1
        if self.head is None:
            self.head = node
            self.curr = self.head  
        else:
            self.curr.next = node
            self.curr = self.curr.next
        return "Node added"

    def display_list(self):
        itr = self.head
        string1 = ''
        while itr:
            string1 += '->' + (str(itr.value))
            itr = itr.next
        print(string1)

    def peek_linkedlist(self):
        return self.head.value

    def pop_from_start(self):
        if self.length == 0:
            return "List Empty"
        else:
            self.length -= 1
            print(f"{self.head.value} popped")
            self.head = self.head.next

    def delete_at_index(self, index):
        if index > self.length:
            return "Index out of bounds"
        else:
            itr = self.head
            curr_idx = 0
            while curr_idx != index-2:
                itr = itr.next

            temp = itr.next.value
            itr.next = itr.next.next

            return f"{temp} popped at index {index}"

    def insert_at_index(self, index, value):
        new_node = Node(value)

        if index > self.length:
            return "Index out of bounds"
        else:
            itr = self.head
            curr_idx = 0
            while curr_idx != index - 1:
                itr = itr.next
                curr_idx += 1

            new_node.next = itr.next
            itr.next = new_node

            return f"{value} inserted at index {index}"

    def detect_cycle(self, node):
        slow = fast = node
        itr = node
        while fast or (slow == fast):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                while itr != slow:
                    itr = itr.next
                return itr.value

        return False
