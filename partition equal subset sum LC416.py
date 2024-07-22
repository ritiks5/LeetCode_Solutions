# partition equal subset sum LC416 PY

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0 :
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1, -1, -1):
            dp2 = set()
            for t in dp:
                if t + nums[i] == target : return True
                dp2.add(t+nums[i])
                dp2.add(t)
            dp = dp2

        return False
