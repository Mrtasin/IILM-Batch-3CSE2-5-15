def twoSumSimple(num, target):
    x = 0
    l = len(num)
    while x < l:
        z = x+1
        while z < l:
            if num[x] + num[z] == target:
                return [x,z]
            z += 1
        x += 1
    return []

def twoSum(nums, target):
    index = 0
    m = {}
    for val in nums:
        res = target - val
        if res in m:
            return [m[res],index]
        m[val] = index
        index += 1
    return []


n = [2,7,13,15]
print(twoSum(n,9))