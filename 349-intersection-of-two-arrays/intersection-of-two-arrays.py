class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        len1 = len(nums1)
        len2 = len(nums2)
        finalArr = []

        if len1 <= len2:

            for i in range(len1):
                if nums1[i] in nums2:
                    finalArr.append(nums1[i])

        else: 

            for i in range(len2):
                if nums2[i] in nums1:
                    finalArr.append(nums2[i])

        finalArr = list(set(finalArr))

        return finalArr

            
        