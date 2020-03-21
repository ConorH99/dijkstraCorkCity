class Element:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        outstr = "(%i, %i)" % (self.key, self.value)
        return outstr

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

class Heap:

    def __init__(self):
        self.structure = []
        self.root = None
        self.size = 0
        self.last = None

    def __str__(self):
        outstr = "["
        for i in self.structure:
            outstr += str(i)
        outstr += "]"
        return outstr

    def add(self, key, value):
        element = Element(key, value)
        self.structure.append(element)
        self.root = 0
        self.size += 1
        self.last = self.size - 1
        if self.size > 1:
            self.bubbleUp(self.last)
        return element
            

    def bubbleUp(self, index):
        if index != self.root:
            parent = (index-1) // 2
            if self.structure[index].key < self.structure[parent].key:
                self.structure[index], self.structure[parent] = self.structure[parent], self.structure[index]
            self.bubbleUp(parent)

heap = Heap()
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

