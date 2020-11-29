class Solution(object):
    def kthSmallest(self, root, k):
        count = self.get_nodes(root.left)
        while count + 1 != k:
            if count + 1 < k:
                root = root.right
                k = k - count - 1
            else:
                root = root.left
            count = self.get_nodes(root.left)
        return root.val

    def get_nodes(self, root):
        if not root:
            return 0
        return 1 + self.get_nodes(root.left) + self.get_nodes(root.right)

    class Solution_4(object):
        def kthSmallest(self, root, k):
            self.k = k
            self.num = 0
            self.in_order(root)
            return self.num

        def in_order(self, root):
            if root.left:
                self.in_order(root.left)
            self.k -= 1
            if self.k == 0:
                self.num = root.val
                return
            if root.right:
                self.in_order(root.right)