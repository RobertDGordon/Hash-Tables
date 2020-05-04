["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"]

hash_table_size = 8

hash_table = [None] * hash_table_size

def myhash(s):
    str_bytes = s.encode()
    total = 0

    for b in str_bytes:
        total += b

        # total &= 0xfffffffff
        # total &= 0xffffffffffffffffff

    return total

def hash_index(s):
    h = myhash(s)

    return h % hash_table_size

def put(key, value):
    index = hash_index(key)
    hash_table[index] = value

def get(key):
    index = hash_index(key)
    return hash_table[index]

def delete(key):
    index = hash_index(key)
    hash_table[index] = None

if __name__ == "__main__":
    #command line
    # print(hash_index("Hello"))
    # print(hash_index("foobar"))
    # print(hash_index("cats"))
    # print(hash_index("beej"))
    put("Hello", 37)
    put("foobar", 128)
    put("cats", "dogs")
    print(hash_table)
    print(get("Hello"))
    print(get("cats"))
    delete("hello")
    print(get("Hello"))
