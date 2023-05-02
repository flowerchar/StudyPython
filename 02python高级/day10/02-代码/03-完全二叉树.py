class Node(object):
    """节点类"""
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class BinaryTree(object):
    """二叉树"""
    def __init__(self, node=None):
        self.root = node

    def add(self, item):
        """添加节点"""
        pass

    def bradh_travel(self):
        """广度优先遍历"""
        pass



