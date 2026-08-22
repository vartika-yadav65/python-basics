nums1 = {1, 2, 3, 4, 5}
nums2 = {4, 5, 6, 7}

print("Union:", nums1 | nums2)
print("Common:", nums1 & nums2)
print("Only in nums1:", nums1 - nums2)

nums1.add(10)
print(nums1)