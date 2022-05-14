class Block:
    def __init__(self, data=None, prev_hash=0):
        self._next = None
        self._data = data
        self._prev_hash = prev_hash
        self._hash = hash((self._data, self._prev_hash))
        self.print_hash()

    #the init method should save the data parameter into self_data and
    # create a new self_hash using a hashed combination of data and
    # prev_hash. self._next should be none

    def add_block(self, data, prev_hash=0):
        current = self
        if current._next is None:
            # print(current._data)
            current._next = Block(data, self._hash)
            return

        while current._next is not None:
            current = current._next
            # print(current._data)

        if current._next is None:
            current._next = Block(data, self._hash)



    def print_hash(self):
        print(f'Transaction added. New hash is {self._hash}')



    def block_checker(self): #i think this is the foundation of replay,
        # you need to make it so it reshashes the self.data and
        # self.previous, and then checks it against the current self.hash to
        # see if anything has changed
        print()
        print("Replaying Blockchain")
        current = self
        # print(self._data)
        while current._next is not None:
            print(current._data)
            current = current._next
            # print(current._data)

        if current._next is None:
            print(current._data)
            print(f'Final hash is {current._hash}')

    #the add_block method will traverse the list to search for the last
    # block. It will create a new Block object using the data parameter  and
    # self_hash of the last block, and install that block into self._next of
    # the last block.

    def replay(self, prev_hash=0):
        # print()
        print("Replaying Blockchain")
        # you need to make it so it reshashes the self.data and
        # self.previous, and then checks it against the current self.hash to
        # see if anything has changed
        current = self
        # print(self._data)
        while current._next is not None:
            hash_check = hash((current._data, current._prev_hash))
            # print(hash_check)
            # print(current._hash)
            if hash_check == current._hash:
                print(current._data)
                current = current._next
            else:
                print("Blockchain is Corrupted!!")
                # print(current._data)
                return

        if current._next is None:
            hash_check = hash((current._data, current._prev_hash))
            if hash_check == current._hash:
                print(current._data)
                print("Blockchain verified. End of Transactions")
                print(f'Final hash is {current._hash}')
                return

            else:
                print("Blockchain is Corrupted!!")
                # print(current._data)
                return


    # the add_block method will traverse the l

    #the replay method will traverse the list. At each block it first
    # verifies self._hash. If the calculate value does not match self_hash,
    # print an error message and hald. Otherwise print self._data and
    # continue to the next code.

    #do i need to overload the hash function?
    # def __hash__(self):
    #     return hash(self._data, self._prev_hash)


