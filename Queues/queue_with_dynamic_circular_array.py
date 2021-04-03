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
            self.resize()
        self.que.append(data)
        if self.front == None:
            self.front = self.rear = 0
        else:
            self.rear = self.length
        self.length += 1

    def resize(self):
        new_queue = list(self.que)
        self.limit = 2 * self.limit
        self.que = new_queue

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
                self.rear =  self.length - 1
    
    def print_queue(self):
        print(f'Queue Items : {self.que}')
        print(f'Front : {self.que[self.front]}')
        print(f'Rear : {self.que[self.rear]}')

    
que = Queue(5)
que.en_queue(10)
que.en_queue(20)
que.en_queue(30)
que.en_queue(40)
que.en_queue(50)
que.en_queue(20)
que.de_queue()
que.en_queue(100)
que.de_queue()
que.print_queue()