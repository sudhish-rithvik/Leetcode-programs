class Solution(object):
    def bstToGst(self, root):
        self.total = 0

        def dfs(node):
            if node is None:
                return

            # Visit larger values first
            dfs(node.right)

            self.total += node.val
            node.val = self.total

            dfs(node.left)

        dfs(root)
        return root