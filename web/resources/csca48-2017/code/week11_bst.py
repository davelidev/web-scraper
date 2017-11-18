import random


class BSTNode(object):
    """A node in a binary tree."""

    def __init__(self, d, left=None, right=None):
        '''(BSTNode, object, BSTNode, BSTNode) -> NoneType
        Create a BSTNode with data 'd' and children left and right.
        '''

        self.data = d
        self.left = left
        self.right = right

    def contains(self, search_obj):
        '''(BSTNode, obj) -> bool
        Return True iff the tree rooted at this node has a node which contains
        search_obj
        '''
        if(self.data == search_obj):
            result = True
        elif(self.data > search_obj):
            #  if it's in here, it must be in our left subtree
            if(self.left):
                result = self.left.contains(search_obj)
            else:
                result = False
        else:
            #  if it's in here, it must be in our right subtree
            if(self.right):
                result = self.right.contains(search_obj)
            else:
                result = False
        return result

    def print_tree(self, indent=""):
        '''(BSTNode, str) -> NoneType
        Print the tree rooted at BSTNode root. Print str indent (which
        consists only of whitespace) before the root value; indent more
        for the subtrees so that it looks nice.
        '''
        if(self.right):
                        self.right.print_tree(indent + "\t")

        print (indent + str(self.data))
        if(self.left):
                        self.left.print_tree(indent + "\t")

    def insert_node(self, new_data):
        '''(BSTNode,object) -> NoneType
        Insert data into the binary tree rooted at this node.
        '''
        # need to decide whether to go left or right
        if(new_data < self.data):
            # we need to go left, if we have a left node, just tell it to
            # insert this into its subtree
            if(self.left):
                self.left.insert_node(new_data)
            # if we don't have a left node, well we do now
            else:
                self.left = BSTNode(new_data)
        else:
            # same deal on the right side
            if(self.right):
                self.right.insert_node(new_data)
            else:
                self.right = BSTNode(new_data)

    def _remove_rightmost(self):
        '''(BSTNode) -> (obj, BSTNode)
        Remove the rightmost node from the tree rooted at root, and return
        it's value, and the root of this tree after it has been removed
        '''
        if(not self.right):
            # found the leaf, remove it and return its value
            result = (self.data, self.left)
        else:
            # keep searching the right branch
            (ret_val, self.right) = self.right._remove_rightmost()
            result = (ret_val, self)
        return result

    def get_smallest(self):
        '''(BSTNode) -> obj
        Return the value of the smallest node in the tree rooted at self
        '''
        # this one's easy. If I have a left child, I'm not the smallest
        # if I don't, I am.
        if(self.left):
            result = self.left.get_smallest()
        else:
            result = self.data
        return result

    def delete_node(self, remove_obj):
        '''(BSTNode, obj) -> BSTNode
        Delete the node containing remove_obj from the tree rooted at root
        Return the new tree rooted at root
        '''
        retval = self
        #  remove from subtrees
        if(self.data <= remove_obj):
            # it must be in our right subtree
            if(self.right):
                self.right = self.right.delete_node(remove_obj)
        else:
            if(self.left):
                self.left = self.left.delete_node(remove_obj)
        #  if we're the node that needs to be deleted
        if(self.data == remove_obj):
            # if we don't have 2 subtrees, we're in luck, just pass back
            #  the subtree we do have so our parent can link to it instead
            #  of us
            if(not self.left):
                retval = self.right
            elif(not self.right):
                retval = self.left
            else:
                #  we've got 2 subtrees, so we have to replace ourselves
                #  with one of our descentants, and then delete that descendant

                # option # 1, find the value of the node we want to replace
                # take its value and delete it
                new_value = self.right.get_smallest()
                self.data = new_value
                self.right.delete_node(new_value)

                # option # 2, get the node to delete and its parent
                # we have 2 subtrees, so we need to replace ourselves with
                # something
                # (prev_value, left_subtree) = self.left._remove_rightmost()
                # self.data = prev_value
                # self.left = left_subtree
        return retval


class BSTree():

    def __init__(self):
        self._root = None

    def print_tree(self):
        if(self._root):
            self._root.print_tree()

    def insert(self, new_val):
        if(self._root):
            self._root.insert_node(new_val)
        else:
            self._root = BSTNode(new_val)

    def search(self, search_val):
        if(self._root):
            result = self._root.contains(search_val)
        else:
            result = False
        return result

    def delete(self, delete_val):
        if(self._root):
            self._root.delete_node(delete_val)

if (__name__ == '__main__'):
    my_bst = BSTree()
    for i in range(10):
        my_bst.insert(random.randint(1, 20))
    my_bst.print_tree()
    for i in range(5):
        search_val = random.randint(1, 20)
        print("Does the tree contain ", search_val, "?",
              my_bst.search(search_val))

    for i in range(5):
        delete_val = random.randint(1, 20)
        print("Deleting: ", delete_val)
        my_bst.delete(delete_val)

    my_bst.print_tree()
