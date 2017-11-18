class StackEmptyError(Exception):
    '''An error to raise when someone tries to remove something
    from an empty stack'''

class QueueEmptyError(Exception):
    '''An error to raise when someone tries to dequeue from an
    empty queue'''

class ContainerEmptyError(Exception):
    '''An error to raise when someone tries to remove an item from
    an empty container'''

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
        RAISES: ContainerEmptyError if this container is empty
        '''

    def is_empty(self):
        '''(Container) -> bool
        Return True iff this container is empty
        '''


class Stack(Container):
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
        try:
            ret_item = self.pop()
        except StackEmptyError:
            raise ContainerEmptyError("Can't remove an item from an empty container")
        return ret_item

class Queue(Container):
    '''A First In First Out (FIFO) Queue of items'''

    def __init__(self):
        '''(Queue) -> NoneType
        Create a new, empty queue
        '''
        # REPRESENTATION INVARIANT
        # _contents is a list containing the elements of this queue
        # len(_contents) is the number of elements in the queue
        # if len(_contents) > 0:
        #    _contents[0] is the item at the front of the queue
        #    _contents[-1] is the item at the end of the queue
        #    if(i > j)
        #        _contents[i] is after _contents[j] in the queue
        self._contents = []

    def enqueue(self, new_obj):
        '''(Queue, object) -> NoneType
        add new_obj to the end of this queue
        '''
        self._contents.append(new_obj)

    def dequeue(self):
        '''(Queue) -> object
        Remove and return the front item in the queue.
        RAISES: QueueEmptyError if the queue is empty
        '''
        if(self.is_empty()):
            raise QueueEmptyError("Can't dequeue from an empty queue")
        ret_item = self._contents[0]
        self._contents = self._contents[1:]
        return ret_item

    def is_empty(self):
        '''(Queue) -> bool
        Return True iff this queue is empty
        '''
        return self._contents == []

    def put(self, new_object):
        '''(Queue, obj) -> NoneType
        Add new_object to this conatiner
        '''
        self.enqueue(new_object)

    def get(self):
        '''(Queue) -> obj
        Remove and return an object (order not guarnteed) from this container
        RAISES: ContainerEmptyError if this container is empty
        '''
        if(self.is_empty()):
            raise ContainerEmptyError("Can't remove an item from an empty container")
        else:
            return self.dequeue()



class NeckStack(Stack):
    '''A Stack which removes the 2nd to top element rather than the top element
    if there are 2 or more elements in the stack'''

    def pop(self):
        '''(NeckStack) -> NoneType
        Remove and return the 2nd highest element in the stack if there are
        2 or more elements in the stack. If there's only 1 element, remove
        and return that one
        RAISES: StackEmptyError if the neckstack is empty
        '''
        if(self.is_empty()):
            raise StackEmptyError("Can't pop from an empty stack")
        top_item = Stack.pop(self)
        # if there's only 1 item, just return it
        if(self.is_empty()):
            ret_item = top_item
        # if are 2 items, return the 2nd one from the top, and put the top
        # one back on
        else:
            second_item = Stack.pop(self)
            self.push(top_item)
            ret_item = second_item
        return ret_item

    def get(self):
        '''(NeckStack) -> obj
        Remove and return an object (order not guarnteed) from this container
        RAISES: ContainerEmptyError if this container is empty
        '''
        if(self.is_empty()):
            raise ContainerEmptyError("Can't remove an item from an empty container")
        else:
            return self.pop()

if(__name__ == "__main__"):
    my_container = Queue()
    my_container.put("A")
    my_container.put("B")
    my_container.put("C")
    my_container.put("D")
    my_container.put("E")
    my_container.put("F")
    my_container.put("G")
    while(not my_container.is_empty()):
        print(my_container.get())
    #try one more to test that the right error is raised
    try:
        my_container.get()
    except ContainerEmptyError:
        print("Sorry... container was empty")