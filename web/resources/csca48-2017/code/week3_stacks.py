class StackEmptyError(Exception):
    '''An error to raise when someone tries to remove something
    from an empty stack'''


class Container():
    '''A container that holds objects, we don't know the order in which
    objects will come out'''

    def __init__(self):
        '''(Container) -> NoneType
        Create a new empty container
        '''

    def put(self, new_object):
        '''(Container, obj) -> NoneType
        Add new_object to this container
        '''

    def get(self):
        '''(Container) -> obj
        Remove and return an object (order not guarnteed) from this container
        '''

    def is_empty(self):
        '''(Container) -> bool
        Return True iff this container is empty
        '''


class StackA(Container):
    '''A last-in, first-out (LIFO) stack of items'''

    def __init__(self):
        '''(Stack) -> NoneType
        Create a new, empty stack.
        '''
        # REPRESENTATION INVARIANT
        # _contents is a list containing the elements of this stack
        # len(_contents) is the number of elements in the stack
        # if len(_contents) > 0:
        #    _contents[0] is the bottom of the stack
        #    _contents[-1] is the top of the stack
        #    if(i > j)
        #        _contents[i] is above _contents[j] in the stack
        self._contents = []

    def push(self, new_obj):
        '''(Stack, object) -> NoneType
        Place new_obj on top of this stack.
        '''
        self._contents.append(new_obj)

    def pop(self):
        '''(Stack) -> object
        Remove and return the top item in this stack.
        RAISES: StackEmptyError if the stack is empty
        '''
        if(self.is_empty()):
            raise StackEmptyError("Can't pop from an empty stack")
        ret_item = self._contents[-1]
        self._contents = self._contents[:-1]
        return ret_item

    def is_empty(self):
        '''(Stack) -> bool
        Return True iff this stack is empty
        '''
        return self._contents == []
        # could have also done
        # return len(self._contents) == 0

    def put(self, new_object):
        '''(Stack, obj) -> NoneType
        Add new_object to this stack
        '''
        # this method is necessary if we want to implement the container ADT
        self.push(new_object)

    def get(self):
        '''(Stack) -> obj
        Remove and return an object (order not guarnteed) from this stack
        '''
        return self.pop()


class StackB(Container):
    '''A last-in, first-out (LIFO) stack of items'''

    def __init__(self):
        '''(Stack) -> NoneType
        Create a new, empty Stack.
        '''
        # REPRESENTATION INVARIANT
        # _contents is a list containing the elements of this stack
        # len(_contents) is the number of elements in the stack
        # if len(_contents) > 0:
        #    _contents[-1] is the bottom of the stack
        #    _contents[0] is the top of the stack
        #    if(i < j)
        #        _contents[i] is above _contents[j] in the stack
        self._contents = []

    def push(self, new_obj):
        '''(Stack, object) -> NoneType
        Place new_obj on top of this stack.
        '''
        # Store the item to the beginning of the list
        # (this is a bad idea, but we're doing it anyway)
        self._contents.insert(0, new_obj)

    def pop(self):
        '''(Stack) -> object
        Remove and return the top item in this stack.
        RAISES: StackEmptyError if the stack is empty
        '''
        if(self.is_empty()):
            raise StackEmptyError("Can't pop from an empty stack")
        ret_item = self._contents[0]
        self._contents = self._contents[1:]
        return ret_item

    def is_empty(self):
        '''(Stack) -> bool
        Return True iff this stack is empty.'''

        return self._contents == []

    def put(self, new_object):
        '''(Stack, obj) -> NoneType
        Add new_object to this stack
        '''
        # this method is necessary if we want to implement the container ADT
        self.push(new_object)

    def get(self):
        '''(Stack) -> obj
        Remove and return an object (order not guarnteed) from this stack
        '''
        return self.pop()


class StackC(Container):
    '''A last-in, first-out (LIFO) stack of items'''

    def __init__(self):
        '''(Stack) -> NoneType
        Create a new, empty stack.
        '''
        # REPRESENTATION INVARIANT
        # _contents is a dictionary mapping positions in the stack
        # to elements at that position
        # _height is the number of elements in the stack
        # if _height > 0:
        #    _contents[_height - 1] is the top the stack
        #    _contents[0] is the bottom item on the stack
        #    if(i > j)
        #        _contents[i] is above _contents[j] on the stack
        #    if(i > _height)
        #        _contents[i] is not an item on the stack
        self._contents = {}
        self._height = 0

    def push(self, new_obj):
        '''(Stack, object) -> NoneType
        Place new_obj on top of this stack.
        '''
        self._contents[self._height] = new_obj
        self._height += 1

    def pop(self):
        '''(Stack) -> object
        Remove and return the top item in this stack.
        RAISES: StackEmptyError if the stack is empty
        '''
        # to pop, we don't actually need to remove the items from
        # the dictionary, as any further push will simply over-write
        # the next key, and we're using height to check for emptiness
        if(self.is_empty()):
            raise StackEmptyError("Can't pop from an empty stack")
        self._height -= 1
        return self._contents[self._height]

    def is_empty(self):
        '''(Stack) -> bool
        Return True iff this stack is empty
        '''
        # this is a good example of where we need to know how the rest
        # of the code in our class works, if we used
        # return self.contents == {}
        # it would fail, because of the way we implemented pop
        return self._height == 0

    def put(self, new_object):
        '''(Stack, obj) -> NoneType
        Add new_object to this stack
        '''
        # this method is necessary if we want to implement the container ADT
        self.push(new_object)

    def get(self):
        '''(Stack) -> obj
        Remove and return an object (order not guarnteed) from this stack
        '''
        return self.pop()


class NeckStack(StackA):
    '''A Stack which removes the 2nd to top element rather than the top element
    if there are 2 or more elements in the stack'''

    def pop(self):
        '''(NeckStack) -> NoneType
        Remove and return the 2nd highest element in the stack if there are
        2 or more elements in the stack. If there's only 1 element, remove
        and return that one'''
        if(self.is_empty()):
            raise StackEmptyError("Can't pop from an empty stack")
        top_item = StackA.pop(self)
        # if there's only 1 item, just return it
        if(self.is_empty()):
            ret_item = top_item
        # if are 2 items, return the 2nd one from the top, and put the top
        # one back on
        else:
            second_item = StackA.pop(self)
            self.push(top_item)
            ret_item = second_item
        return ret_item

if(__name__ == "__main__"):
    my_stack = NeckStack()
    my_stack.push("A")
    my_stack.push("B")
    my_stack.push("C")
    my_stack.push("D")
    my_stack.push("E")
    my_stack.push("F")
    my_stack.push("G")
    for i in range(8):
        try:
            print(my_stack.pop())
        except StackEmptyError:
            print("Sorry, the stack was empty")

