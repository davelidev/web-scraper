## An example of implementing a container using a stack
## with a composition model

from week2_stacks import StackA  # <-- change to the other types of stacks


class Container():
    '''A container that holds objects, we don't know the order in which
    objects will come out'''

    def __init__(self):
        '''(Container) -> NoneType
        Create a new empty container
        '''
        self._my_stack = StackA()  # <-- you'll need to change this as well

    def put(self, new_object):
        '''(Container, obj) -> NoneType
        Add new_object to this container
        '''
        self._my_stack.push(new_object)

    def get(self):
        '''(Container) -> obj
        Remove and return an object (order not guarnteed) from this container
        '''
        return self._my_stack.pop()

    def is_empty(self):
        '''(Container) -> bool
        Return True iff this container is empty
        '''
        return self._my_stack.is_empty()

if(__name__ == "__main__"):
    my_container = Container()
    for next_item in ['Alice', 'Bob', 'Carol', 'Dave']:
        my_container.put(next_item)
    while(not my_container.is_empty()):
        print(my_container.get())
    # example of breaking abstraction, this will fail
    # depending on which type of stack is used
    for next_item in ['Alice', 'Bob', 'Carol', 'Dave']:
        my_container.put(next_item)
    while(my_container._my_stack._contents != []):
        print(my_container.get())
