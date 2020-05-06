"""
this file defines a HashTable class that implements the Map abstract data type.
The getitem and setitem methods have been overloaded to allow indexing (d[i]).

"""

class HashTable:

    def __init__(self, size=11, debug=False):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.debug = debug

    def store(self, key, value):
        hashVal = self.hash(key, self.size)
        if self.debug:
            print("Hash Val of (%s) = %s" % (key, hashVal))
        # if no stored key, add new key:value pair
        if self.slots[hashVal] is None:
            self.slots[hashVal] = key
            self.data[hashVal] = value
        # if key exists, replace value with new value
        elif self.slots[hashVal] == key:
            self.data[hashVal] = value
        # if slot filled with different key, find open slot
        else:
            nextSlot = self.rehash(hashVal, self.size)
            while self.slots[nextSlot] is not None and self.slots[nextSlot] != key:
                 nextSlot = self.rehash(nextSlot, self.size)
            # if no stored key, add new key:value pair
            if self.slots[nextSlot] is None:
                self.slots[nextSlot] = key
                self.data[nextSlot] = value
            # if key exists, replace value with new value
            else:
                self.data[nextSlot] = value

    # implement modulo method
    def hash(self, key, slots):
        return key % slots

    # look for empty slot, check every third to prevent clustering
    def rehash(self, hashVal, slots):
        return (hashVal + 1) % self.size

    def get(self, key):
        init = self.hash(key, self.size)
        value = None; index = init
        finished = False; found = False
        # search from start slot until empty slot, value, or start slot found
        while self.slots[index] is not None and not found and not finished:
            if self.slots[index] == key:
                found = True
                value = self.data[index]
            else:
                index = self.rehash(index, self.size)
                if index is init:
                    finished = True
        return value

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.store(key, value)

    def __str__(self):
        print("Hash table:")
        print("-----------")
        map = zip(self.slots, self.data)
        mapstring = "["
        for key, value in enumerate(map):
            mapstring += str(key)
            mapstring += ":"
            mapstring += str(value)
            if key != self.size - 1:
                mapstring += ", "
        return mapstring + "]"

if __name__=="__main__":
    table = HashTable(debug=False)
    test = ['cat', 'dog', 'lion', 'fish', 'bird', 'tiger', 'cow', 'goat', 'chicken', 'pig']
    for word in test:
        key = sum([ord(char) for char in word])
        table[key] = word
    print(table)
    print("\nChanging a key:value pair...\n")
    table[329] = 'duck'
    print(table)
