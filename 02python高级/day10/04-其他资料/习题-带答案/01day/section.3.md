# 企业面试题

####1. 输入两棵二叉树A，B，判断B是不是A的子结构。

```python
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def is_subtree(self, a, b):
        if not b:
            return True
        if not a or a.val != b.val:
            return False
        return self.is_subtree(a.left, b.left) and self.is_subtree(a.right, b.right)

```

####2. 将给定的二叉树变换为其镜像

```python
def Mirror(self, root):
    if not root:
        return
    if not root.left and not root.right:
        return
    root.left, root.right = root.right, root.left
    self.Mirror(root.left)
    self.Mirror(root.right)
    return root
```

#### 3. 二叉树的深度

```python
def TreeDepth1(self, pRoot):
    if not pRoot:
    return 0
    left = self.TreeDepth(pRoot.left)
    right = self.TreeDepth(pRoot.right)
    return left + 1 if left > right else right + 1
```

####4. 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左、右子树的深度相差不超过1，那么它就是平衡二叉树。

```python
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        if abs(self.TreeDepth(pRoot.left)-self.TreeDepth(pRoot.right))>1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left+1, right+1)
```

