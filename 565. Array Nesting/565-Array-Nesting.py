class Solution(object):
    def __init__(self):
        pass

    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        for num_index in range(len(nums)):
            if nums[num_index] == 0:
                if num_index == 0:
                    longest = 1
                continue
            else:
                length = 1
                head, next_element, former_element = num_index, nums[num_index], num_index
                while next_element != head and next_element != 0:
                    length += 1
                    nums[former_element] = 0
                    former_element = next_element
                    next_element = nums[next_element]
                if length > longest:
                    longest = length
        return longest



if __name__ == '__main__':
    s = Solution()
    test = [5,4,0,3,1,6,2]
    print(s.arrayNesting(test))