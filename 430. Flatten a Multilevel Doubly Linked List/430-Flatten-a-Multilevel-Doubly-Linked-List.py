
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def __init__(self):
        pass

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return head
        curr = head
        while curr:
            if curr.child:
                pre = curr.child
                while pre.next:
                    pre = pre.next
                pre.next = curr.next
                if pre.next:pre.next.prev = pre
                
                curr.next =curr.child
                if curr.next:curr.next.prev = curr
                curr.child = None
            curr = curr.next
        return head


if __name__ == "__main__":
    s = Solution()

    def connect(node1, node2, pos=0):
        if pos == 0:
            node1.next = node2
            node2.prev = node1
        else:
            node1.child = node2

    nodes = [Node(i, None, None, None) for i in range(13)]
    connect(nodes[1], nodes[2])
    connect(nodes[2], nodes[3])
    connect(nodes[3], nodes[4])
    connect(nodes[4], nodes[5])
    connect(nodes[5], nodes[6])

    connect(nodes[7], nodes[8])
    connect(nodes[8], nodes[9])
    connect(nodes[9], nodes[10])

    connect(nodes[11], nodes[12])

    connect(nodes[3], nodes[7], pos=1)
    connect(nodes[8], nodes[11], pos=1)

    n = s.flatten(nodes[1])
    result = []
    while n != None:
        result.append(n.val)
        n = n.next
    print(result)


