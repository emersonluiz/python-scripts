#!/usr/bin/env python

class Node(object):

    leftNode = None
    rightNode = None

    def __init__(self, value):
        self.value = value

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setLeftNode(self, leftNode):
        self.leftNode = leftNode

    def getLeftNode(self):
        return self.leftNode

    def setRightNode(self, rightNode):
        self.rightNode = rightNode

    def getRightNode(self):
        return self.rightNode

class BinaryTree(object):

    root = None

    def getHeight(self):
        return self._getHeight(self.root)

    def _getHeight(self, root):
        if root is None:
            return 0

        leftHeight = self._getHeight(root.getLeftNode())
        rightHeight = self._getHeight(root.getRightNode())
        if (leftHeight > rightHeight):
            return leftHeight + 1
        else:
            return rightHeight + 1

    def length(self):
        return self._length(self.root)

    def _length(self, root):
        if root is None:
            return 0
        lenLeftNode = self._length(root.getLeftNode())
        lenRightNode = self._length(root.getRightNode())
        return lenLeftNode + lenRightNode + 1

    def insert(self, value):
        self._insert(self.root, value)

    def _insert(self, node, value):
        if self.root is None:
            self.root = Node(value)
        else:
            if value < node.getValue():
                if node.getLeftNode() is not None:
                    self._insert(node.getLeftNode(), value)
                else:
                    n = Node(value)
                    node.setLeftNode(n)
            elif value > (node.getValue()):
                if node.getRightNode() is not None:
                    self._insert(node.getRightNode(), value)
                else:
                    node.setRightNode(Node(value))

    def printTree(self):
        if self.root is None:
            print "Empty Tree"
        else:
            self._print(self.root)

    def _print(self, node):
        if node.getLeftNode() is not None:
            self._print(node.getLeftNode())
        if node.getRightNode() is not None:
            self._print(node.getRightNode())
        print "NODE:", node.getValue()


b = BinaryTree()
b.insert(23)
b.insert(2)
b.insert(7)
b.insert(6)
b.insert(30)
b.insert(40)
b.insert(77)
print "HEIGHT:", b.getHeight()
print "LENGTH:", b.length()
print "-" * 9
b.printTree()