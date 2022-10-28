class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        if self.items == []:
            return True
        return False

s = Stack()
s.push("Abdullah")
s.push("Arfan")
s.push("Aziz")
s.push("Shahab")
s.push("Sabib")
s.push("jaw jaw")
s.push("Sohel")

#if we want to pop all the value then the operation is down below: 

# while not s.is_empty():
#     item = s.pop()
#     print(item)

print(s.pop())

