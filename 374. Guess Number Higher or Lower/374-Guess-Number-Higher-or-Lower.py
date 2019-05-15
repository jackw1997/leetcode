# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

pick = 1

def guess(num):
    if num > pick:
        return -1
    elif num == pick:
        return 0
    else:
        return 1

class Solution(object):

    def __init__(self):
        pass


    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while True:
            my_guess = int((low + high) / 2)
            ans = guess(my_guess)
            if ans == 0:
                return my_guess
            elif ans == 1:
                low = my_guess + 1
            else:
                high = my_guess - 1

if __name__ == "__main__":
    s = Solution()
    print(s.guessNumber(10))