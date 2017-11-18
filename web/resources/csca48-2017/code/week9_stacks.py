class PrintableStack:
    '''A last-in, first-out (LIFO) stack of items'''

    def __init__(self, name):
        '''(Stack,str) -> NoneType
        Create a new, empty stack with a name
        '''
        self._contents = []
        self._name = name

    def __str__(self):
        '''(Stack) -> str
        Return a string representation of this stack
        '''
        return self._name + str(self._contents)

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

    def size(self):
        '''(Stack) -> int
        Return the number of elements in the stack
        '''
        return len(self._concents)
