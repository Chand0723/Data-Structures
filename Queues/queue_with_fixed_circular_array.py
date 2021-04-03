class Queue:
    def __init__(self, limit=10):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.length = 0

    def is_empty(self):
        return self.length <= 0

    def en_queue(self, data):
        if self.length >= self.limit:
            print('Queue Overflow')
            return -1
        else:
            self.que.append(data)    

        if self.front == None:
            self.front = self.rear = 0
        else:
            self.rear = self.length
        self.length += 1

    def de_queue(self):
        if self.length <= 0:
            print('Queue Underflow')
            return -1
        else:
            self.que.pop(0)
            self.length -= 1
            if self.length == 0:
                self.front = self.rear = None
            else:
                self.rear = self.length-1

    def print_queue(self):
        print(f'Queue Items : {self.que}')
        print(f'Front : {self.que[self.front]}')
        print(f'Rear : {self.que[self.rear]}')

            
        
que = Queue(5)
que.en_queue(1)
que.en_queue(2)
que.en_queue(3)
que.en_queue(4)
que.en_queue(5)
que.en_queue(2)
que.de_queue()
que.en_queue(100)
que.de_queue()
que.print_queue()

# print(que.que)
# print(que.front)
# print(que.rear)