from week6_containers import *

class BinTreeNode:
    """
    A node in a binary tree.
    """

    def __init__(self, data, left=None, right=None):
        """ (BinTreeNode, str, BinTreeNode, BinTreeNode) -> NoneType

        Initialize a new BinTreeNode with data, left and right children.
        """

        self.data = data
        self.left = left
        self.right = right


def traverse(root, container):
    output = ""
    container.put(root)
    while(not container.is_empty()):
        current = container.get()
        output += current.data + " "
        if(current.left):
            container.put(current.left)
        if(current.right):
            container.put(current.right)
    return output



if __name__ == "__main__":

    # what does the following tree look like?
    root = BinTreeNode("A",
        BinTreeNode("B",
            BinTreeNode("C", None, None),
            BinTreeNode("D",
                        BinTreeNode("H")
                        , None)),
        BinTreeNode("E",
            BinTreeNode("F", None, None),
            BinTreeNode("G", None, None)))

    my_container = Queue()
    print(traverse(root, my_container))
