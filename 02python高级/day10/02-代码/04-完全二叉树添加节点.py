class Node(object):
    """节点类"""
    def  __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class BinaryTree(object):
    """完全二叉树"""
    def __init__(self, node=None):
        self.root = node

    def add(self, item):
        """添加节点"""

        if self.root == None:
            self.root = Node(item)
            return

        # 队列
        queue = []
        # 从尾部添加数据
        queue.append(self.root)

        while True:
            # 从头部取出数据
            node = queue.pop(0)
            # 判断左节点是否为空
            if node.lchild == None:
                node.lchild = Node(item)
                return
            else:
                queue.append(node.lchild)

            if node.rchild == None:
                node.rchild = Node(item)
                return
            else:
                queue.append(node.rchild)

    def breadh_travel(self):
        """广度优先遍历"""

        if self.root == None:
            return

        # 队列
        queue = []
        # 添加数据
        queue.append(self.root)

        while len(queue)>0:
            # 取出数据
            node = queue.pop(0)
            print(node.item, end="")

            # 判断左右子节点是否为空
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)

if __name__ == '__main__':
    tree = BinaryTree()
    tree.add("A")
    tree.add("B")
    tree.add("C")
    tree.add("D")
    tree.add("E")
    tree.add("F")
    tree.add("G")
    tree.add("H")
    tree.add("I")
    tree.breadh_travel()






























