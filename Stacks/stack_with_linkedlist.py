class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head == None

    def push(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop(self):
        if self.head == None:
            print('Stack Underflow')
        else:
            self.head = self.head.next
            self.length -= 1

    def print_stack(self):
        node_list = []
        current = self.head
        while current != None:
            node_list.append(current.data)
            current = current.next  
        print(node_list)

    def peek(self):
        if self.head == None:
            print('Empty Stack')
        else:
            print(self.head.data)

st = Stack()
st.push(20)
st.push(30)
st.push(40)
st.push(50)
st.push(60)
st.push(70)
st.push(10)

st.print_stack()

st.pop()

st.print_stack()

st.peek()
print(st.length)