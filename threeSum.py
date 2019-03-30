# -*- coding: UTF-8 -*-


class Solution(object):
    def threesum(self, nums):
        nums2 = sorted(nums)
        r = []
        i = 0
        while i < len(nums2) - 2:
            if nums2[i] > 0:
                break
            c = -nums2[i]
            left = i+1
            right = len(nums2) - 1
            while right > left:
                sum = nums2[left] + nums2[right]
                if sum == c:
                    r.append([nums2[i],nums2[left],nums2[right]])
                    while left + 1 < len(nums2) and nums2[left] == nums2[left + 1]:
                        left = left+1
                    while right - 1 >=0 and nums2[right] == nums2[right - 1]:
                        right = right-1
                    left = left + 1
                    right = right - 1
                elif sum > c:
                    right = right - 1
                else:
                    left = left + 1
            while i+1 < len(nums2) and nums2[i] == nums2[i+1]:
                i = i + 1
            i = i + 1
        return r

solution = Solution()
print(solution.threesum([-1,0,1,2,-1,-4]))