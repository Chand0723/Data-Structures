class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.prev = None
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        new_node.next = None
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        new_node.prev = current
        self.tail = new_node
        self.length += 1

    def insert_at_pos(self, pos, data):
        if pos < 1 or pos > self.length:
            print('Enter a valid position')

        if pos == 1:
            self.insert_at_begining(data)
        elif pos == self.length:
            self.insert_at_end(data)
        else:
            new_node = Node(data)
            count = 1
            current = self.head
            while count < (pos-1):
                count += 1
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next = new_node
            current.next.prev = new_node
        self.length += 1

    
    def print_list(self):
        node_list = []
        current = self.head
        while current != None:
            node_list.append(current.data)
            current = current.next
        print(node_list)

    def delete_first_node(self):
        if self.length == 0:
            print('List is empty')
        else:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1

    def delete_last_node(self):
        if self.length == 0:
            print('List is empty')
        else:
            current = self.head
            previous = self.head
            while current.next != None:
                previous = current
                current = current.next
            previous.next = None
            self.tail = previous
            self.length -= 1

    def delete_at_pos(self, pos):
        if pos > self.length or pos < 1:
            print('Enter a valid postion')

        if pos == 1:
            self.delete_first_node()
            self.length -= 1
        elif pos == self.length:
            self.delete_last_node()
            self.length -= 1
        else:
            count = 1
            current = self.head
            previous =  self.head
            while count < pos:
                count += 1
                previous = current
                current = current.next
            previous.next = current.next
            current.next.prev = previous
            self.length -= 1


dll = DoublyLinkedList()
dll.insert_at_begining(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_end(4)        
dll.insert_at_end(5)        

dll.print_list()
dll.insert_at_pos(3, 100)
dll.print_list()

dll.delete_first_node()
dll.delete_last_node()
dll.delete_at_pos(2)
dll.print_list()

print(f'Length of DLL : {dll.length}')