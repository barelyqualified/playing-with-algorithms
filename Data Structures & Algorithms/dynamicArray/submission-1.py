class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = 0
        self.data = [None] * capacity
        print(f'initialized array. capacity: {self.capacity}, data size: {len(self.data)}')


    def get(self, i: int) -> int:
        if self.data[i] == None:
            return 0
        else:
            return int(self.data[i])


    def set(self, i: int, n: int) -> None:
        if self.data[i] == None:
            self.used = self.used + 1
        self.data[i] = n


    def pushback(self, n: int) -> None:
        if self.capacity == self.used:
            print("resized")
            self.resize()
        self.set(self.getSize(), n)

    def popback(self) -> int:
        self.used = self.used - 1
        return self.get(self.used)

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        self.data = self.data + ([None] * self.capacity)

    def getSize(self) -> int:
        return self.used
        
    def getCapacity(self) -> int:
        return self.capacity 