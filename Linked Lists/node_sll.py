class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None