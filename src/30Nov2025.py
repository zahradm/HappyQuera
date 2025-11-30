class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_dict: dict[int, int] = {}
        i = 0
        while i < len(nums):
            app = unique_dict.get(nums[i], "")
            if not app or nums[i] not in unique_dict.keys():
                unique_dict[nums[i]] = 1
                i += 1
            else:
                if nums[i] in unique_dict.keys():
                    unique_dict[nums[i]] += 1
                    nums.pop(i)

        return len(unique_dict.keys())
