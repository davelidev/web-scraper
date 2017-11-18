class ListIndexError(Exception):
    '''An error to be rasied when someone tries to access an invalid
    element of the list'''


class Node():
    '''A node in a linked list'''
    def __init__(self, data, next_node=None):
        # Note that since Nodes are generally not publicly accessed anyway
        # and it saves us having to use accessor methods millions of times
        # we're going to make our data and next_node variables public
        # this means that we're stuck with this setup forever, but
        # it seems like a worthwhile trade

        # REPRESENTATION INVARIANT
        # data is the data content of this node
        # if this is the last node in the linked list:
        #     next_node is None
        # otherwise:
        #     next_node is the address of the node to which this node 'points'
        self.data = data
        self.next_node = next_node


class List():
    '''An extensible list of items'''

    def __init__(self):
        '''(List) -> NoneType
        Create a new empty list
        '''
        # REPRESENTATION INVARIANT

        # If the list is empty
        #    self._head = self._tail = None
        # otherwise
        #    self._head is the address of the first node in the list
        #    self._tail is the address of the last node in the list
        #    if nodes A and B are both nodes in this linked list
        #    and A comes before B (i.e., A is closer to the head of the list
        #    than B)
        #        A.next_node[.next_node]* = B
        #        ([.next_node]* means 0 or more repetitions of .next_node)
        self._head = None
        # self._tail = None
        # in this implementation, we haven't used the _tail so that we could
        # show examples of finding the end of the list. I encourage you to
        # try adding the _tail functionality on your own

    def __str__(self):
        '''(List) -> str
        Return a string reprensetation of this list
        '''
        output_str = ""
        current = self._head
        # loop through the list adding the data of each node
        # until we reach the end of the list
        while(current is not None):
            output_str += str(current.data) + "->"
            current = current.next_node
        # now we've got an extra -> on the end of our output
        # so let's remove that
        output_str = output_str[:-2]
        return output_str

    def append(self, new_item):
        '''(List, object) -> NoneType
        Add new_item to the end of this list
        '''
        new_node = Node(new_item)
        # if the list is empty, we just point the head to our new node
        if(self.is_empty()):
            self._head = new_node
        # otherwise, loop through the list until current is pointing to the
        # last node in the list
        else:
            current = self._head
            while(current.next_node is not None):
                current = current.next_node
            # now have current (last node in the list)'s pointer point to our
            # new node
            current.next_node = new_node

    def prepend(self, new_item):
        '''(List, object) -> NoneType
        Add new_item to the beginning of this list
        '''
        # create a new node that points to the current head
        new_node = Node(new_item, self._head)
        # now have the head point to our new node
        self._head = new_node

    def _find_index(self, i):
        '''(List, int) -> Node
        Return a reference to the node at index i
        RAISES: ListIndexException if there is no ith node in this list
        '''
        if(i < 0):
            raise ListIndexError("Can't have an index < 0")

        current = self._head
        current_index = 0
        # loop through the list until we either get to the node we're
        # looking for, or run off the end of the list
        while(current is not None and current_index < i):
            current = current.next_node
            current_index += 1
        # if we ran off the end of the list, raise an error, otherwise
        # return the node. One caveat: if the index was 0, then we will
        # be pointing to None
        if(current is None and i != 0):
            raise ListIndexError("Not a valid index")
        else:
            return current

    def insert(self, new_item, index):
        '''(List, object, int) -> NoneType
        Add new_item to the list at index, moving all items after index
        one place over
        RAISES: ListIndexError if index < 0 or index > length of the list
        '''
        new_node = Node(new_item)
        # special case, if we're adding to the front of the list
        if(index == 0):
            self.prepend(new_item)
        else:
            # since we now have the very helpful _find_index method, we can
            # just use that to find the node 1 before where we want to insert
            # and if no such node exists, it will raise the errors for us
            current = self._find_index(index - 1)
            # so current now points to the node one spot before where we want
            # to insert our new node, so let's get the link for everything
            # that will come after our new node
            after = current.next_node
            # now we have current pointing to the node that goes before
            # our new node, and after pointing to the node that goes
            # after our new node, so let's link them up
            current.next_node = new_node
            new_node.next_node = after

    def get_first(self):
        '''(List) -> object
        Remove and return the first item in this list
        RAISES: ListIndexException if the list is empty
        '''
        ret_item = self._head.data
        # this one is pretty easy, just point the head of the list
        # to the 2nd node (if there is no 2nd node, then the first
        # node will point to None, so we'll wind up with an empty list
        # as expected
        self._head = self._head.next_node
        return ret_item

    def get_last(self):
        '''(List) -> object
        Remove and return the last item in this list
        RAISES: ListIndexException if the list is empty
        '''
        # special case: list is empty
        if(self.is_empty()):
            raise ListIndexException("Can't remove from an empty list")

        # find the last node in the list (key here, need to look ahead
        # so that we stop one short)

        current = self._head
        # special case: list has 1 element (in this case, we can't stop
        # with current being the node before the one we want to remove)
        if(current.next_node is None):
            # list only had 1 item, so just return its value and set
            # head to None
            ret_item = current.data
            self._head = None
        else:
            # loop until we're one away from the end of the list
            while(current.next_node.next_node is not None):
                current = current.next_node
            # now we're at the 2nd to last node, so return the last node's
            # data, and remove the last node
            ret_item = current.next_node.data
            current.next_node = None
        return ret_item

    def retrieve(self, index):
        '''(List, int) -> object
        Remove and return the item at index in the list
        RAISES: ListIndexError if index < 0 or index >= length of the list
        '''
        # special case: item to remove is at index 0 (since we can't
        # stop one before in order to unlink)
        if(index == 0):
            ret_item = self.get_first()
        else:
            # find the node that's 1 before the one we want to unlink
            current = self._find_index(index - 1)
            # one thing to watch out for... if they've asked us to remove
            # an index that 1 greater than the last index in our list,
            # _find_index will happily return to us the index - 1 element
            # but we'd fail trying to get the last piece of data, so
            # we need to check for that here
            if(current.next_node is None):
                raise ListIndexError("Not a valid index")
            else:
                # now we know that we're pointing to the node one before
                # the one we want to delete
                # get the data to return
                ret_item = current.next_node.data
                # now un-link the node from the chain
                current.next_node = current.next_node.next_node
        return ret_item

    def is_empty(self):
        '''(List) -> bool
        Return True iff this list is empty
        '''
        return self._head is None

if(__name__ == "__main__"):
    l = List()
    print(l)
    l.append("A")
    l.append("B")
    l.append("C")
    print(l)
    l.prepend("Z")
    l.prepend("Y")
    l.prepend("X")
    print(l)
    l.insert("D", 3)
    print(l)
    l.insert("E", 2)
    print(l)
    l.insert("F", 1)
    print(l)
    l.insert("G", 0)
    print(l)
    l.insert("H", 10)
    print(l)
    print(l.get_first())
    print(l.get_first())
    print(l)
    print(l.get_last())
    print(l.get_last())
    print(l)
    print(l.retrieve(3))
    print(l)
    print(l.retrieve(0))
    print(l)
    print(l.retrieve(4))
    print(l)
