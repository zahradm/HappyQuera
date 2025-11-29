class Solution(object):
    def max_area(self, height) -> int:
        for i in range(len(height)):
            if height[i] < height[i + 1]:
                start = i + 1
                break
            elif height[i] == height[i + 1]:
                start = i
                break
        for j in range(len(height)):
            if height[j] == 0:
                end = j - 1
                break
            else:
                end = j
        value = min(height[start], height[end])
        aixs = end - start
        return value * aixs
