class Solution(object):
    def __init__(self):
        pass

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        last, i = len(nums) - 1, len(nums) - 1
        while i >= 0:
            if i + nums[i] >= last:
                last = i
            i -= 1
        return last <= 0


if __name__ == "__main__":
    s = Solution()
    test = [2, 3, 1, 1, 4]
    print(s.canJump(test))