class Circular():
    def __init__(self, length):
        self.n = length
        self.queue = [0] * length
        self.front = -1
        self.rear = -1
    
    def enqueue(self, item):
        if self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
        elif self.is_full():
            print("Circular Queue is full ! ")
        else:
            self.rear = (self.rear+1) % self.n
            self.queue[self.rear] = item
    
    def dequeue(self):
        if self.is_empty():
            print("Circular Queue is Empty ! ")
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            print(self.queue[self.front])
            self.front = (self.front + 1) % self.n
    
    def display(self):
        i = self.front
        if self.is_empty():
            print("Circular Queue is Empty ! ")
        else:
            print("Queue is : ")
            while i != self.rear:
                print(self.queue[i])
                i = (i+1) % self.n
            print(self.queue[self.rear])
        
    def is_empty(self):
        if self.front == -1 and self.rear == -1:
            return True
        return False
    
    def is_full(self):
        if (self.rear+1) % self.n == self.front:
            return True
        return False


q = Circular(3)
q.enqueue("abd")
q.enqueue("arfan")
q.enqueue("ab")
q.enqueue("al")
q.dequeue()
q.display()
q.dequeue()
q.dequeue()
