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

    def __str__(self):
        '''(Node) -> str
        Return a string representation of the linked list starting at
        this node'''
        # add the data for this node
        result = str(self.data)
        # if there are more nodes in the list, recursively get their string
        # representation and add it to ours
        if(self.next_node is not None):
            result += " -> " + str(self.next_node)
        return result

    def add_to_tail(self, new_item):
        '''(Node, object) -> None
        Add a new node containing new_item to the tail of the linked list
        rooted at this node
        '''
        # if we're the last node in the linked list, create a new node and
        # link to it
        if(self.next_node is None):
            self.next_node = Node(new_item)
        # if we're not the last node, just let the next node deal with it
        else:
            self.next_node.add_to_tail(new_item)

    def delete_tail(self):
        '''(Node) -> (Node, object)
        Remove the last node in the linked list rooted at this node,
        return the head of the modified list and the data that
        was held in the tail node
        '''
        # if we're the last node, just return None (so the node
        # before us will link to that instaed of linking to us)
        if(self.next_node is None):
            result = (None, self.data)
        # otherwise, tell our next node to delete its tail, and
        # return a link to the head of the modified list, and
        # link to that
        else:
            (self.next_node, ret_val) = self.next_node.delete_tail()
            # don't forget that we have to return a pointer
            # to ourselves
            result = (self, ret_val)
        return result

    def insert_at_index(self, new_obj, index):
        '''(Node, object, int) -> Node
        Insert a new node containing new_obj as the indexth
        elemnt of the linked list rooted at this node
        '''
        # if we're supposed to insert at the next node, do so
        if(index == 1):
            self.next_node = Node(new_obj, self.next_node)
        # otherwise, just insert into the linked list rooted at
        # the next node with index -1
        else:
            # special case: we've hit the end of the linked list
            if(self.next_node is None):
                raise ListIndexError("Not a valid index")
            else:
                self.next_node.insert_at_index(new_obj, index-1)

    def remove(self, index):
            '''(Node, int) -> NoneType
            Remove the index'th node from the linked list rooted at this node
            and return its contents
            '''
            # if the next node is the one to delete, then do so
            if(index == 1):
                # special case: if we're at the end of the list and being asked
                # to delete something
                # then raise an error
                if(self.next_node is None):
                    raise IndexError("Not a valid index")
                else:
                    ret_item = self.next_node.data
                    # now simply un-link the next node
                    self.next_node = self.next_node.next_node
            # if we need to delete something further down, then let
            # the recursion take care of it
            else:
                # special case: we hit the end of the list before running
                # out of indices this means they asked for something
                # beyond the end of the list
                if(self.next_node is None):
                    raise ListIndexError("Not a valid index")
                else:
                    # deleting the ith node in this linked list, is just
                    # deleting the i-1th node in the linked list
                    # rooted at next_node
                    ret_item = self.next_node.remove(index-1)
            return ret_item


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
        if(self._head is None):
            result = ""
        else:
            result = str(self._head)
        return result

    def append(self, new_item):
        '''(List, object) -> NoneType
        Add new_item to the end of this list
        '''
        # if the list is empty, then add a new node
        if(self._head is None):
            self._head = Node(new_item)
        # if the list isn't empty, just tell the head node
        # to deal with the problem
        else:
            self._head.add_to_tail(new_item)

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
        if(index < 0):
            raise ListIndexError("Not a valid index")
        # special case, if we're adding to the front of the list
        if(index == 0):
            self.prepend(new_item)
        else:
            # since we know the index is >= 1, we can just let the
            # head node deal with it
            if(self._head is None):
                # special case #2, trying to insert into a non-zero index of an
                # empty list (need this as the else case assue
                raise ListIndexError("Not a valid index")
            else:
                self._head.insert_at_index(new_item, index)

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
        # otherwise, just let the head node deal with it
        else:
            (self._head, ret_val) = self._head.delete_tail()
            return ret_val

    def retrieve(self, index):
        '''(List, int) -> object
        Remove and return the item at index in the list
        RAISES: ListIndexError if index < 0 or index >= length of the list
        '''
        if(index < 0):
            raise ListIndexError("Not a valid index")
        # special case: item to remove is at index 0 (since we can't
        # stop one before in order to unlink)
        if(index == 0):
            ret_item = self.get_first()
        else:
            if(self._head is None):
                # special case #2: trying to delete from an empty list
                raise ListIndexError("Not a valid index")
            else:
                ret_item = self._head.remove(index)
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
