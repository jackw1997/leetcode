xrange = range

class Solution(object):
    def __init__(self):
        pass

    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        def first(elem):
            return elem[0]
        for i in xrange(len(B)):
            B[i] = (B[i], i)
        B.sort(key=first)
        A.sort()
        ans = [0] * len(A)
        j, d = 0, -1
        for i in xrange(len(A)):
            if A[i] > B[j][0]:
                ans[B[j][1]] = A[i]
                j += 1
            else:
                ans[B[d][1]] = A[i]
                d -= 1
        return ans

if __name__ == "__main__":
    testcase = [[2,7,11,15], [1,10,4,11]]
    testresult = [2,11,7,15]
    s = Solution()
    if testresult == s.advantageCount(testcase[0], testcase[1]):
        print("Accepted")
    else:
        print("Wrong Answer")