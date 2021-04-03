class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.head == None

    def en_queue(self, data):
        new_node = Node(data)
        if self.length <= 0:
            self.head = self.tail = new_node
        else:
            new_node.next = None
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
            self.tail = new_node
        self.length += 1

    def de_queue(self):
        if self.head == None:
            print('Queue is Empty')
        else:
            self.head = self.head.next
            self.length -= 1
    
    def print_list(self):
        node_list = []
        current = self.head
        while current != None:
            node_list.append(current.data)
            current = current.next  
        print(node_list)

que = Queue()
que.en_queue(100)
que.en_queue(200)
que.en_queue(300)
que.en_queue(400)
que.en_queue(500)
que.de_queue()
que.print_list()
print(f'Front : {que.head.data}')
print(f'Rear : {que.tail.data}')



