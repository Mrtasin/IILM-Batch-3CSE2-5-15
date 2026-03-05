class Solution:
    def trap(self, h: List[int]) -> int:
        size = len(h)
        rightMax = [0] * size

        rightMax[size - 1] = h[size - 1]

        for index in range(size - 2, -1, -1):
            rightMax[index] = max(rightMax[index + 1], h[index])

        ans = 0
        leftMax = h[0]

        for index in range(0, size):
            leftMax = max(leftMax, h[index])
            ans += min(leftMax, rightMax[index]) - h[index]

        return ans
