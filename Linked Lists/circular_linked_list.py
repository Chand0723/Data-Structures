## unfinshed implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node
        self.length += 1

    def print_list(self):
        node_list = []
        current = self.head
        while current.next != self.head:
            node_list.append(current.data)
        print(node_list)

    
cll = CircularLinkedList()
cll.insert_at_beginning(1)
cll.insert_at_beginning(2)

#cll.insert_at_end(2)
#cll.insert_at_end(3)

cll.print_list()
print(cll.length)