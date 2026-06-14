class Stack_using_array:
    def __init__(self):
        self.size = 10
        self.stack = [0] * self.size
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            print("Stack overflow")
            return
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
            return
        data = self.stack[self.top]
        self.top -= 1
        return data
    
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return
        data = self.stack[self.top]
        return data

    def is_empty(self):
        return self.top == -1
    
    def display(self):
        if self.top == -1:
            print("Stack is underflow")
            return
        temp = self.top
        while temp > -1:
            print(self.stack[temp],end="->")
            temp -= 1
        print("Null")
    
if __name__ == "__main__":
    obj = Stack_using_array()
    print(obj.is_empty())
    obj.pop()
    obj.push(10)
    obj.push(20)
    obj. display()
    obj.push(30)
    obj.display()
    obj.pop()
    obj.display()
    print(obj.is_empty())