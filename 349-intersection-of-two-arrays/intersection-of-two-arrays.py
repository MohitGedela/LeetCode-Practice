class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        num1Set = set(nums1)
        output = set()
        for i in nums2:
            if i in num1Set:
                if i not in output:
                    output.add(i)
   

        return list(output)