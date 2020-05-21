class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity = 32):
        self.capacity = capacity
        self.size = 0
        self.storage = [None] * self.capacity

    def fnv1a(self, key, seed = 0):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        #FNV-1a Hash Function
        hash = offset_basis + seed
        for char in key:
            hash = hash ^ ord(char)
            hash = hash * FNV_prime
        return hash


    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1a(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #increment size of hash table
        self.size += 1
        
        #compute index using hash function
        hash_index = self.hash_index(key)

        #if bucket at index is empty, create new node and insert
        node = self.storage[hash_index]
        if node is None:
            self.storage[hash_index] = HashTableEntry(key, value)
            return

        #if not empty, collision occured
        #iterate to end of list and add new node at end
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        #compute hash
        #iterate linked listed of nodes, continue until found or end
        #if key is not found, return none
        #else remove node from linked list
        index = self.hash_index(key)
        node = self.storage[index]
        prev = node
        if node.key == key:
            self.storage[index] = node.next
            return

        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            print(f'{key} not found')
            return None
        else:
            self.size -= 1
            prev.next = node.next
            

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        #compute index
        index = self.hash_index(key)

        #go to bucket at index
        node = self.storage[index]
        
        #iterate the nodes in linked list until key or end is found
        while node is not None and node.key != key:
            node = node.next
        
        #return the value if found, or none if not found
        if node is None:
            return None
        else:
            return node.value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        #create new table double size
        self.capacity *= 2
        new_table = [None] * (self.capacity)

        #iterate through current list
        for index in range(len(self.storage)):
            node = self.storage[index]
            #if there is a linked list, iterate through and rehash
            while node is not None:
                new_hash_index = self.hash_index(node.key)
                new_table[new_hash_index] = node
                node = node.next
        
        self.storage = new_table

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
