class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length += 1

    def print_list(self):
        list_node = []
        if self.length == 0:
            print('List is Empty')
        else:
            current = self.head
            list_node.append(current.data)
            while current.next != self.head:
                current = current.next
                list_node.append(current.data)
            print(list_node)

    def delete_from_front(self):
        if self.length == 0:
            print('List is Empty')
        else:
            if self.head != self.tail:
                self.head = self.head.next
                self.tail.next = self.head
                self.length -= 1
            else:
                self.head = self.tail = None
                self.length -= 1
        
    def delete_from_last(self):
        if self.length == 0:
            print('List is empty')
        else:
            if self.head != self.tail:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                self.tail = current
                self.tail.next = self.head
                self.length -= 1
            else:
                self.head = self.tail = None
                self.length -= 1

    
    
cll = CircularLinkedList()
cll.insert_at_beginning(2)
cll.insert_at_beginning(1)
cll.insert_at_end(3)
cll.insert_at_end(4)
cll.insert_at_end(5)

cll.print_list()

cll.delete_from_front()
cll.delete_from_last()
cll.print_list()
print(cll.length)