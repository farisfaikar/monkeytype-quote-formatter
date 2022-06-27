def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# source
# geeksforgeeks - Fibonacci
# code
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
# source
# geeksforgeeks - Factorial
# code
class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data
# source
# geeksforgeeks - Doubly Linked List
# code
def push(self, new_data):
    new_node = Node(data=new_data)
    new_node.next = self.head
    new_node.prev = None
    if self.head is not None:
        self.head.prev = new_node
    self.head = new_node
# source
# geeksforgeeks - Doubly Linked List
# code
def append(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
        self.head = new_node
        return
    last = self.head
    while last.next:
        last = last.next
    last.next = new_node
    new_node.prev = last
    return
# source
# geeksforgeeks - Doubly Linked List
# code
def __str__(self):
    cur = self.head.next
    out = ""
    while cur:
        out += str(cur.value) + "->"
        cur = cur.next
    return out[:-3]
# source
# geeksforgeeks - Stack
# code
def peek(self):
    if self.isEmpty():
        raise Exception("Peeking from an empty stack")
    return self.head.next.value
# source
# geeksforgeeks - Stack
# code
def push(self, value):
    node = Node(value)
    node.next = self.head.next
    self.head.next = node
    self.size += 1
# source
# geeksforgeeks - Stack
# code
def pop(self):
    if self.isEmpty():
        raise Exception("Popping from an empty stack")
    remove = self.head.next
    self.head.next = self.head.next.next
    self.size -= 1
    return remove.value
# source
# geeksforgeeks - Stack
# code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
# source
# geeksforgeeks - Stack
# code
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
# source
# geeksforgeeks - Merge Sort
# code
def inorder(temp):
    if (not temp):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)
# source
# geeksforgeeks - Binary Search Tree
# code
s = "*-A/BC-/AKL"
stack = []
operators = set(['+', '-', '*', '/', '^'])
s = s[::-1]
for i in s:
    if i in operators:
        a = stack.pop()
        b = stack.pop()
        temp = a + b + i
        stack.append(temp)
    else:
        stack.append(i)
print(*stack)
# source
# geeksforgeeks - Prefix Postfix Conversion
# code
def printList(self):
    temp = self.head
    while (temp):
        print(temp.data)
        temp = temp.next
# source
# geeksforgeeks - Linked List
# code
def insertAfter(self, prev_node, new_data):
    if prev_node is None:
        print("The given previous node must inLinkedList.")
        return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node
# source
# geeksforgeeks - Linked List
# code
def append(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
        self.head = new_node
        return
    last = self.head
    while (last.next):
        last = last.next
    last.next = new_node
# source
# geeksforgeeks - Linked List
# code
def getNthNode(self, head, position, llist):
    count = 0
    if (head):
        if count == position:
            print(head.data)
        else:
            llist.getNthNode(head.next, position - 1, llist)
    else:
        print("Index Doesn't exist")
# source
# geeksforgeeks - Linked List
# code
def addToEmpty(self, data):
    if (self.last != None):
        return self.last
    temp = Node(data)
    self.last = temp
    self.last.next = self.last
    return self.last
# source
# geeksforgeeks - Circular Singly Linked List
# code
def addBegin(self, data):
    if (self.last == None):
        return self.addToEmpty(data)
    temp = Node(data)
    temp.next = self.last.next
    self.last.next = temp
    return self.last
# source
# geeksforgeeks - Circular Singly Linked List
# code
def addEnd(self, data):
    if (self.last == None):
        return self.addToEmpty(data)
    temp = Node(data)
    temp.next = self.last.next
    self.last.next = temp
    self.last = temp
    return self.last
# source
# geeksforgeeks - Circular Singly Linked List
