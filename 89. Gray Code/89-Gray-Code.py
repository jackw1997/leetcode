class Solution(object):
    def __init__(self):
        pass

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        FormerResult = [0]
        TwoPower = 1
        for _ in range(n):
            FormerLength = len(FormerResult)
            for element_index in range(FormerLength):
                FormerResult.append(FormerResult[FormerLength-1-element_index] + TwoPower)
            TwoPower <<= 1
        return FormerResult


if __name__ == "__main__":
    s = Solution()
    test = 2
    print(s.grayCode(test))