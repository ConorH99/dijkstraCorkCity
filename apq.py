from pq import *

class Element(Element):
    def __init__(self, key, value, index):
        super().__init__(key, value)
        self.index = index

    def __str__(self):
        outstr = "(%i, %i (%i))" % (self.key, self.value, self.index)
        return outstr

class APQ(Heap):

    def __init__(self):
        super().__init__()

    def add(self, key, value):
        self.size += 1
        self.last = self.size - 1
        element = Element(key, value, self.last)
        self.structure.append(element)
        self.root = 0
        if self.size > 1:
            self.bubbleUp(self.last)
        return element

    def remove_min(self):
        min = self.min()
        self.structure[self.root].index, self.structure[self.last].index = self.structure[self.last].index, self.structure[self.root].index 
        self.structure[self.root], self.structure[self.last] = self.structure[self.last], self.structure[self.root]
        self.structure.pop(self.last)
        self.last -= 1
        self.size -= 1
        self.bubbleDown(self.root)
        return min

    def updateKey(self, element, newKey):
        if newKey < element.key:
            element.key = newKey
            self.bubbleUp(element.index)
        else:
            element.key = newKey
            self.bubbleDown(element.index)

    def bubbleUp(self, index):
        if index != self.root:
            parent = (index-1) // 2
            if self.structure[index].key < self.structure[parent].key:
                self.structure[index].index, self.structure[parent].index = self.structure[parent].index, self.structure[index].index
                self.structure[index], self.structure[parent] = self.structure[parent], self.structure[index]
                self.bubbleUp(parent)

    def bubbleDown(self, index):
        if 2 * index + 2 <= self.size:
            lc = 2 * index + 1
            rc = 2 * index + 2
            if self.structure[lc].key < self.structure[rc].key:
                swap = 2 * index + 1
            else:
                swap = 2 * index + 2
        elif 2 * index + 1 <= self.size:
            swap = 2 * index + 1
        else:
            return None
        if self.structure[index].key > self.structure[swap].key:
            self.structure[index].index, self.structure[swap].index = self.structure[swap].index, self.structure[index].index
            self.structure[index], self.structure[swap] = self.structure[swap], self.structure[index]
            self.bubbleDown(swap)
            

heap = APQ()
e1 = heap.add(25, 1)
print(heap)
e2 = heap.add(27, 1)
print(heap)
e3 = heap.add(29, 1)
print(heap)
e4 = heap.add(28, 1)
print(heap)
e5 = heap.add(35, 1)
print(heap)
e6 = heap.add(49, 1)
print(heap)
e7 = heap.add(43, 1)
print(heap)
e8 = heap.add(37, 1)
print(heap)
e9 = heap.add(22, 1)
print(heap)
e10 = heap.add(50, 1)
print(heap)
e11 = heap.add(12, 1)
print(heap)
e12 = heap.add(33, 1)
print(heap)
heap.remove_min()
print(heap)
heap.remove_min()
print(heap)
heap.updateKey(e4, 23)
print(heap)