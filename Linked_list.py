class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def insert_at_index(self, index, data):
        if index < 0:
            return
        if index == 0:
            self.insert_at_begining(data)
        newNode = Node(data)
        temp = self.head
        for _ in range(index-1):
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode


    def delete_by_index(self, index):
        if index < 0:
            return
        if index == 0:
            data = self.head
            self.head = self.head.next
            return data
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        if temp is None or temp.next is None:
            return
        temp.next = temp.next.next

    def delete_by_value(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    def search(self, value):
        if self.head is None:
            return
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("Null")


if __name__ == "__main__":
    l1 = LinkedList()
    l1.display()
    l1.insert_at_begining(10)
    l1.insert_at_begining(20)
    l1.display()
    l1.insert_at_end(5)
    l1.display()


