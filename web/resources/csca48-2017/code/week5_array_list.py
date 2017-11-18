class ListIndexError(Exception):
    '''An error to be raised when someone tries to access an element outside
    the valid boundaries of a list
    '''


class List():
    '''An extensible list of items'''

    def __init__(self):
        '''(List) -> NoneType
        Create a new empty list
        '''
        # we're going to try to do this without using Python's built in
        # list dynamic allocation, so pretending we only had fixed
        # sized arrays

        # REPRESENTATION INVARIANT
        # _contents is a list containing all of the elements in this list
        # in order

        self._contents = []

    def __str__(self):
        '''(List) -> str
        Return a string reprensetation of this list
        '''
        return str(self._contents)

    def append(self, new_item):
        '''(List, object) -> NoneType
        Add new_item to the end of this list
        '''
        # pretend here that we're allocating a new array with space for
        # one more element, and copying everyting over one at a time
        self._contents = self._contents + [new_item]

    def prepend(self, new_item):
        '''(List, object) -> NoneType
        Add new_item to the beginning of this list
        '''
        self._contents = [new_item] + self._contents

    def insert(self, new_item, index):
        '''(List, object, int) -> NoneType
        Add new_item to the list at index, moving all items after index
        one place over
        RAISES: ListIndexError if index < 0 or index > length of the list
        '''
        if(index < 0 or index > len(self._contents)):
            raise ListIndexError
        else:
            # pretend here that we're re-allocating a new array of size
            # 1 greater than the current array's size
            self._contents = (self._contents[:index] + [new_item] +
                              self._contents[index:])

    def get_first(self):
        '''(List) -> object
        Remove and return the first item in this list
        RAISES: ListIndexException if the list is empty
        '''
        if(self.is_empty()):
            raise ListIndexError("Can't remove items from an empty list")
        else:
            ret_item = self._contents[0]
            self._contents = self._contents[1:]
            return ret_item

    def get_last(self):
        '''(List) -> object
        Remove and return the last item in this list
        RAISES: ListIndexException if the list is empty
        '''
        if(self.is_empty()):
            raise ListIndexError("Can't remove items from an empty list")
        else:
            ret_item = self._contents[-1]
            self._contents = self._contents[:-1]
            return ret_item

    def retrieve(self, index):
        '''(List, int) -> object
        Remove and return the item at index in the list
        RAISES: ListIndexError if index < 0 or index >= length of the list
        '''
        if(index < 0 or index >= len(self._contents)):
            raise ListIndexError("Not a valid index")
        else:
            ret_item = self._contents[index]
            # so here imagine that we're allocating a new array with length
            # 1 smaller than our current array and then copying everything
            # over one at a time
            self._contents = self._contents[:index] + self._contents[index+1:]
            return ret_item

    def is_empty(self):
        '''(List) -> bool
        Return True iff this list is empty
        '''
        return self._contents == []

if(__name__ == "__main__"):
    l = List()
    print(l)
    l.append("A")
    l.append("B")
    l.append("C")
    print(l)
    l.insert("X", 1)
    l.insert("Y", 4)
    print(l)
    l.prepend("Z")
    print(l)
    print(l.get_first())
    print(l.get_last())
    print(l.retrieve(2))
    print(l)
    l.get_first()
    l.get_first()
    l.get_first()
    print(l)
