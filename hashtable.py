class HashTable:
    def __init__(self, size):
        self.size = int(size)
        self.values = [None] * self.size

    def __repr__(self):
        """returns a formatted string containing the values in the hash table"""
        return f"HashTable {self.values}"

    def _hash(self, key):
        """
        Return the hashed value using the rolling polynomial algorithm.
        Further reading: https://cp-algorithms.com/string/string-hashing.html

        Note: 
        - The largest value to be returned will be less than size.   
        Remember to compress the return value to fit the table size (tip: You can use the mod operator once more)
       
        Parameters
        ---------
        - key: str
          The key to be hashed
        """
        if key.islower():
            p = 31
            v = ord('a')
        else:
            p = 53
            v = ord('A')  # only 53 if there is upper and lower case 
        m = 1000000009
        hash_value = 0
        pPower = 1

        for i in range(len(key) - 1):
            char_value = ord(key[i]) - v + 1
            hash_value = (hash_value + char_value * pPower) % m
            pPower = (pPower * p) % m 
        
        return hash_value % self.size

    def add(self, key, value):
        """
        Add a value at the index of the hashed key
        """
        index = self._hash(key)
        if self.values[index] == None:
            self.values[index] = value
            print('Data successfully added')
        else:
            print('Unable to add. Destination not empty!')
            

    def get(self, key):
        """
        Get a value at the index of the hashed key
        """
        index = self._hash(key)
        if self.values[index] == None:
            return 'Destination is empty!'
        return self.values[index]

    def update(self, key, value):
        """
        Update a value at the index of the hashed key
        """
        index = self._hash(key)
        if self.values[index] == None:
            print('Unable to update. Destination is empty!')
        else:
            self.values[index] = value
            print('Data successfully updated')
        
    def remove(self, key):
        """
        Remove a value at the index of the hashed key
        """
        index = self._hash(key)
        if self.values[index] == None:
            print('Unable to remove. Destination is empty!')
        else:
            self.values[index] = None
            print('Data successfully removed')

# For testing: 
# ht = HashTable(6)
# ht.add("bye",3)
# print(ht.__repr__())

# ht.update("hi" , 4)
# ht.update("bye", 5)
# print(ht.__repr__())

