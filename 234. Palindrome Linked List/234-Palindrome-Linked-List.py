class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        pass

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        this_node = head
        while this_node:
            stack.append(this_node)
            this_node = this_node.next
        while stack:
            tail = stack.pop()
            if tail.val != head.val:
                return False
            head = head.next
            
        return True


if __name__ == '__main__':
    s = Solution()
    tc = [1, 2]
    head = node = ListNode(tc[0])

    for i in tc[1:]:
        new_node = ListNode(i)
        node.next = new_node
        node = new_node
    
    print(s.isPalindrome(head))