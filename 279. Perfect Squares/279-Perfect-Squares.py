class Solution(object):
    def __init__(self): 
        pass

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        BFS_Queue = [(n,0)]
        Visited_Nums = {}
        squares = [x**2 for x in range(1, int(math.sqrt(n)) + 1)]
        
        while BFS_Queue:
            num = BFS_Queue[0]
            if num[0] == 0:
                return num[1]
            for square in squares:
                if num[0] - square > 0:
                    if not num[0] - square in Visited_Nums:
                        BFS_Queue.append((num[0] - square, num[1] + 1))
                        Visited_Nums[num[0] - square] = num[1] + 1
                elif num[0] == square:
                    return num[1] + 1
            BFS_Queue = BFS_Queue[1:]


if __name__ == "__main__":
    s = Solution()
    r = 0
    for x in range(1, 100):
        r += x ** 2
    test = [12, 13, r]
    for i in test:
        print(s.numSquares(i))
