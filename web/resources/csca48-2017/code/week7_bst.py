class BSTEmptyError(Exception):
    """An error to be raised when trying to manipulate an empty tree
    in an inappropriate way"""


class BinTreeNode:
    """
    A node in a binary tree.
    """

    def __init__(self, data, left=None, right=None):
        """ (BinTreeNode, str, BinTreeNode, BinTreeNode) -> NoneType

        Initialize a new BinTreeNode with data, left and right children.
        """
		# REPRESENTATION INVARIANT
		# data is an object which is the data held in this node
		# left is a node which is the left child of this node
		# right is a node which is the right child of this node
        self.data = data
        self.left = left
        self.right = right


class BST:
    """
    A binary search tree
    """

    def __init__(self):
        """(BST) -> NoneType
        Create a new empty BST
        """
        # REPRESENTATION INVARIANT
        # _root is the root of the binary search tree
        # if the tree is empty _root is None
        # otherwise:
            # for any node n in the tree:
                # n.left[.left|.right]*.data <= n.data
                # n.right[.left|.right]*.dara > n.data
                # [A|B]* = 0 or more iterations of As and Bs
        self._root = None


    def search(self, value):
        """ (BST, str) -> bool

        Return True iff this BST
        contains a node whose data is value.
        """

        curr = self._root
        while curr != None and curr.data != value:
            if value < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        return (curr != None)


    def insert(self, value):
        """ (BST, str) -> NoneType

        Insert a (possibly duplicate) node whose data is value
        into this BST.
        """

        new_node = BinTreeNode(value)

        # look for parent of new node
        curr = self._root
        parent = None
        while curr != None:
            parent = curr
            if value < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        # if empty BST
        if parent == None:
            self._root = new_node
        else:
            # make new node appropriate child of parent
            if value < parent.data:
                parent.left = new_node
            else:
                parent.right = new_node


    def find_smallest(self):
        """(BST) -> (str)

        Return the smallest value in this BST

        RAISES: BSTEmptyError if this BST is empty
        """
        if(self._root is None):
            raise BSTEmptyError("Cannot find the smallest value in an empty tree")

        # finding smallest is same as finding left most
        curr = self._root

        while curr.left != None:
            curr = curr.left

        return curr.data


    def _find(self, value):
        """ (BST, str) -> (BinTreeNode, BinTreeNode)

        Return 2 nodes, the first pointing to a node
        in this BST whose data is value,
        and the second is its parent.

        For each of these nodes,
        return None if it does not exist.
        """

        # search for node whose data is value
        curr = self._root
        parent = None
        while curr != None and curr.data != value:
            parent = curr
            if value < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        # if node not found
        if curr == None:
            result = (None, None)
        else:
            result = (curr, parent)
        return result

    def _find_smallest_and_parent(self, start_node):
        """ (BST) -> (BinTreeNode, BinTreeNode)

        Return a node with the smallest value
        in the sub-tree rooted at start_node, plus its parent.

        REQ: start_node != None
        """

        # finding smallest is same as finding left most
        curr = start_node
        parent = None
        while curr.left != None:
            parent = curr
            curr = curr.left

        return (curr, parent)



    def delete(self, value):
        """ (BST, str) -> NoneType

        Delete a node whose data is value
        from this BST.

        The BST is unchanged if it does not
        contain a node whose data is value.
        """

        (del_node, del_parent) = self._find(value)

        # if there is a node to delete
        if del_node != None:

            # if node to delete has no left child
            if del_node.left == None:
                # if node to delete is root
                if del_parent == None:
                    self._root = del_node.right
                # elif node to delete is a left child
                elif del_parent.left == del_node:
                    del_parent.left = del_node.right
                # else node to delete must be a right child
                else:
                    del_parent.right = del_node.right

            # elif node to delete has no right child
            elif del_node.right == None:
                # if node to delete is root
                if del_parent == None:
                    self._root = del_node.left
                # elif node to delete is a left child
                elif del_parent.left == del_node:
                    del_parent.left = del_node.left
                # else node to delete must be a right child
                else:
                    del_parent.right = del_node.left

            # else node to delete has both left and right children
            else:
                # find node with next bigger value
                (next_bigger, next_parent) = self._find_smallest_and_parent(del_node.right)

                # copy data from next bigger node to node to delete
                del_node.data = next_bigger.data

                # delete next bigger node
                # if next biggest node is right child of node to delete
                if next_parent == None:
                    del_node.right = next_bigger.right
                else:
                    next_parent.left = next_bigger.right



if __name__ == "__main__":

    # let's cheat (breaking our abstraction) and pre-load a tree
    bst_root = BinTreeNode("N",
        BinTreeNode("I",
            BinTreeNode("C",
                BinTreeNode("A", None, None),
                BinTreeNode("H", None, None)),
            BinTreeNode("L", None, None)),
        BinTreeNode("O",
            None,
            BinTreeNode("S", None, None)))

    my_bst = BST()
    my_bst._root = bst_root
    print(my_bst)
    print("---")
    my_bst.insert("D")
    print(my_bst)
    print(my_bst.search("L"))
    print(my_bst.search("Q"))
    print(my_bst.find_smallest())
    print("---")
    my_bst.delete("L")
    my_bst.delete("N")
    my_bst.delete("D")
    my_bst.delete("S")
    my_bst.delete("O")
    my_bst.delete("I")
    my_bst.delete("H")
    my_bst.delete("A")
    my_bst.delete("C")
    my_bst.delete("Q")


    print(my_bst)
