import ctypes

class DynamicArray(object):
    # Object Object Constructor
    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.Array = self.makeArray(self.capacity)
    
    # Returns the length of this array by calling when called by len()
    def __len__(self):
        return self.length

    #Returns the element at Arr[Idx]
    def __getitem__(self, Idx):
        # If not between the index and length, then return error
        if not 0 <= Idx < self.length: 
            return IndexError("Idx is out of bounds")

        return self.Array[Idx]


    # Add element to the end of the array
    def append(self, element):
        # If the length and capacity of array are the same
        if self.length == self.capacity:
            self._resize(2 * self.capacity) # 2x if capacity isn't enough

        self.Array[self.length] = element
        self.length += 1
    
    # Resizes the array to the new capacity
    def _resize(self, newCapacity):
        # Make new array with new capacity
        newArray = self.makeArray(newCapacity)

        # Copy values from old array into new array
        for i in range(self.length):
            newArray[i] = self.Array[i]

        self.Array = newArray
        self.capacity = newCapacity
    
    # Uses ctypes libray to make a new static array
    def makeArray(self, newCapacity):
        return (newCapacity * ctypes.py_object)()

arr = DynamicArray()
arr.append(1)
print(len(arr))
arr.append(2)
arr.append("bob")
print(len(arr))
print(arr[2])