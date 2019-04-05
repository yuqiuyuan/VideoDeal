# -*- CODING:UTF-8 -*- #

class Solussion:
    def threeSumClosest(self, nums, target):
        nums2 = sorted(nums)
        error = target - nums2[0] - nums2[1] - nums2[2]
        for i in range(1, len(nums2) - 1):
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(nums2):
                curSum = nums2[left] + nums2[i] + nums2[right]
                if curSum == target:
                    return target
                elif curSum > target:
                    left = left - 1
                else:
                    right = right + 1
                if abs(target - curSum) < abs(error):
                    error = target - curSum
        return target - error


solussion = Solussion()
print(solussion.threeSumClosest([-3,0,1,2], 1))
