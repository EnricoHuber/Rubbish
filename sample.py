""" Definition of a stack """


class Stack:
    def __init__(self):
        self.Elementi = []

    def push(self, elemento):
        self.Elementi.append(elemento)

    def pop(self):
        return self.Elementi.pop()

    def is_empty(self):
        return self.Elementi == []

    def print(self):
        print(self.Elementi)


x = Stack()
x.push(10)
x.print()
y = x.pop()
print(x.is_empty())
