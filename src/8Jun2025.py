class Solution(object):
    def addTwoNumbers(self, l1: list[int], l2: list[int]) -> list[int]:
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        digit1 = int("".join(map(str, reversed(l1))))
        digit2 = int("".join(map(str, reversed(l2))))

        final_digit = digit1 + digit2
        return list(map(int, str(final_digit)[::-1]))


print(Solution().addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
