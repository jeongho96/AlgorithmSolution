import sys
from collections import deque

class Queue():
    def __init__(self):
        self.li = deque()
    
    def push(self, n):
        self.li.append(n)

    def pop(self):
        print(self.li.popleft() if self.li else -1)
    
    def size(self):
        print(len(self.li))

    def empty(self):
        print(0 if self.li else 1)
        
    def front(self):
        print(self.li[0] if self.li else -1)
        
    def back(self):
        print(self.li[-1] if self.li else -1)

queue = Queue()
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().split()    
    if s[0] == "push":
        queue.push(int(s[1]))
    elif s[0] == "pop":
        queue.pop()
    elif s[0] == "size":
        queue.size()
    elif s[0] == "empty":
        queue.empty()
    elif s[0] == "front":
        queue.front()
    elif s[0] == "back":
        queue.back()