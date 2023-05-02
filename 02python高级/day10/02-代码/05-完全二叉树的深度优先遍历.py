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

    def preorder_travel(self, root):
        """先序遍历 根 左 右"""
        if root is not None:
            print(root.item, end="")
            self.preorder_travel(root.lchild)
            self.preorder_travel(root.rchild)

    def inorder_travel(self, root):
        """中序遍历 左 根 右"""
        if root is not None:
            self.inorder_travel(root.lchild)
            print(root.item, end="")
            self.inorder_travel(root.rchild)

    def postorder_travel(self, root):
        """后序遍历 根 左 右"""
        if root is not None:
            self.postorder_travel(root.lchild)
            self.postorder_travel(root.rchild)
            print(root.item, end="")


if __name__ == '__main__':
    tree = BinaryTree()
    tree.add("0")
    tree.add("1")
    tree.add("2")
    tree.add("3")
    tree.add("4")
    tree.add("5")
    tree.add("6")
    tree.add("7")
    tree.add("8")
    tree.add("9")
    tree.preorder_travel(tree.root)
    print()
    tree.inorder_travel(tree.root)
    print()
    tree.postorder_travel(tree.root)

































