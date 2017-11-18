# here are 3 separate stack classes, all of which conform to the Stack
# ADT, but which are all implemented in very different ways


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
        self._contents = []

    def push(self, new_obj):
        '''(Stack, object) -> NoneType
        Place new_obj on top of this stack.
        '''
        self._contents.append(new_obj)

    def pop(self):
        '''(Stack) -> object
        Remove and return the top item in this stack.
        '''
        return self._contents.pop()

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
        '''

        return self._contents.pop(0)

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
        # we're going to store the stack as a dictionary {k:v}
        # where k = height on stack, v = value
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
        '''
        # to pop, we don't actually need to remove the items from
        # the dictionary, as any further push will simply over-write
        # the next key, and we're using height to check for emptiness
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


if(__name__ == "__main__"):
    # since everything in Python is an object, it's kinda cool that we can
    # do this to test our implementations:
    stack_implementations = [StackA, StackB, StackC]
    for next_imp in stack_implementations:
        print("Now testing with " + str(next_imp))
        my_stack = next_imp()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        print(my_stack.pop())
        print(my_stack.pop())
        print(my_stack.is_empty())
        print(my_stack.pop())
        print(my_stack.is_empty())
