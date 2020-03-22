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

    def remove_min(self):
        min = self.structure[self.root]
        self.structure[self.root], self.structure[self.last] = self.structure[self.last], self.structure[self.root]
        self.structure.pop(self.last)
        self.last -= 1
        self.size -= 1
        self.bubbleDown(self.root)
        return min

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
            self.structure[index], self.structure[swap] = self.structure[swap], self.structure[index]
            self.bubbleDown(swap)



heap = Heap()
e1 = heap.add(25, 1)
print(heap, heap.last)
e2 = heap.add(27, 1)
print(heap, heap.last)
e3 = heap.add(29, 1)
print(heap, heap.last)
e4 = heap.add(28, 1)
print(heap, heap.last)
e5 = heap.add(35, 1)
print(heap, heap.last)
e6 = heap.add(49, 1)
print(heap, heap.last)
e7 = heap.add(43, 1)
print(heap, heap.last)
e8 = heap.add(37, 1)
print(heap, heap.last)
e9 = heap.add(22, 1)
print(heap, heap.last)
e10 = heap.add(50, 1)
print(heap, heap.last)
e11 = heap.add(12, 1)
print(heap, heap.last)
e12 = heap.add(33, 1)
print(heap, heap.last)
heap.remove_min()
print(heap, heap.last)
heap.remove_min()
print(heap, heap.last)

