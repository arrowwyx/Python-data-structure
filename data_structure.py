from http.client import FOUND
from tempfile import TemporaryDirectory
from turtle import position
from matplotlib.pyplot import cla


class stack:
    
    '''用列表实现栈'''

    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def isempty(self):
        return self.items == []

class Queue:

    '''用列表实现队列'''

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

class Deque:

    '''列表实现双端队列'''

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        self.items.append(item)
    
    def addRear(self, item):
        self.items.insert(0, item)
    
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

class Node:

    '''列表实现链表节点'''

    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
    
    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:

    '''链表'''
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def add(self, item):    # 新元素加到列表的头部
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp    # 这两行一定不能互换位置

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
class OrderedList:
    '''由于元素的有序特性，需要修改add和search方法'''
    def __init__(self):
        self.head = None
    
    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

class hashtable:
    '''散列表'''
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size     # slots用于存储键
        self.data = [None] * self.size      # data用于存储值
    def put(self,key,data):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data # 替换
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and\
                    self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data
    def hashfunction(self,key,size):
        return key%size
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
            not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data
    def __getitem__(self,key):
        return self.get(key)
    def __setitem__(self,key,data):
        self.put(key,data)
    
class binarytree:
    def __init__(self,rootobj):
        self.key = rootobj
        self.leftchild = None
        self.rightchild = None
    
    def insertleft(self,newnode):
        if self.leftchild == None:
            self.leftchild = binarytree(newnode)
        else:
            t = binarytree(newnode)
            t.leftchild = self.leftchild
            self.leftchild = t

    def insertright(self,newnode):
        if self.rightchild == None:
            self.rightchild = binarytree(newnode)
        else:
            t = binarytree(newnode)
            t.rightchild = self.rightchild
            self.rightchild = t
    
    def getrightchild(self):
        return self.rightchild
    
    def getleftchild(self):
        return self.leftchild
    
    def setrootval(self,obj):
        self.key = obj
    
    def getrootval(self):
        return self.key