class Solution(object):
    def __init__(self):
        pass

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        CurrentNumCount, index = 1, 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if CurrentNumCount < 2:
                    CurrentNumCount += 1
            else:
                for j in range(CurrentNumCount):
                    nums[index + j] = nums[i-1]
                index += CurrentNumCount
                CurrentNumCount = 1
        for j in range(CurrentNumCount):
            nums[index + j] = nums[-1]
        index += CurrentNumCount
        return index


if __name__ == "__main__":
    s = Solution()
    test = []
    print(s.removeDuplicates(test))