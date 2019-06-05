class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        pass

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
        counter = 0
        while self.stack:
            this_node = self.stack.pop()
            counter += 1
            if counter == k:
                return this_node.val
            tmp = this_node.right
            while tmp:
                self.stack.append(tmp)
                tmp = tmp.left

if __name__ == '__main__':
    s = Solution()
    tc = [5, 3, 6, 2, 4, None, None, 1]
    k = 5

    tc_nodes = []
    for i in range(len(tc)):
        if tc[i] == None:
            tc_nodes.append(None)
        else:
            tc_nodes.append(TreeNode(tc[i]))
    
    for i in range(len(tc_nodes)):
        if tc_nodes[i] == None:
            continue
        if i*2+1 < len(tc_nodes):
            tc_nodes[i].left = tc_nodes[i*2+1]
        if i*2+2 < len(tc_nodes):
            tc_nodes[i].right = tc_nodes[i*2+2]

    print(s.kthSmallest(tc_nodes[0], k))