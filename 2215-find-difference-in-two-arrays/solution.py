def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    n1 = {}
    n2 = {}
    for i in nums1:
        if i not in n1:
            n1[i] = 0
        n1[i] = n1[i] + 1
    for i in nums2:
        if i not in n2:
            n2[i] = 0
        n2[i] = n2[i] + 1
    
    # left is in n1 but not n2, right is in n2 but not in n1
    a = [[],[]]
    for i in n1:
        if i not in n2:
            a[0].append(i)
    for i in n2:
        if i not in n1:
            a[1].append(i)
    return a