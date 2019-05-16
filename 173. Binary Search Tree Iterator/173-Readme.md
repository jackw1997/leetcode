For this question, we use the stack strategy, as well as a DFS searching algorithm. We first push the root and root's left node and root's left node's left node... into the stack. And we continue poping the first element of the stack, and if it has a right node, do the same process for that node.

For determining whether it is empty, we just need to find whether the stack is empty.

The space complexity is O(log n), where n is the total number of nodes in the tree. The average time complexity is O(1) for each search, since visiting the whole tree requires n times of "next" operation, and each node will be only pushed and poped from the stack once.