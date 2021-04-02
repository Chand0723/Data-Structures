class Stack:
    def __init__(self, limit=10):
        self.stk = []
        self.limit = limit
        self.length = 0
    
    def is_empty(self):
        return self.length == 0

    def push(self, data):
        if self.length >= self.limit:
            print('Stack Overflow')
        else:
            self.stk.append(data)
            self.length += 1

    def pop(self):
        if self.length == 0:
            print('Stack Underflow')
        else:
            self.stk.pop()
            self.length -= 1
    
    def size(self):
        return self.length

    def peek(self):
        return self.stk[-1]

    def print_stack(self):
        print(self.stk)


st = Stack(5)
st.pop()
st.push(10)
st.push(20)
st.push(30)
st.push(40)
st.push(50)
st.push(60)

st.print_stack()

st.pop()
st.print_stack()