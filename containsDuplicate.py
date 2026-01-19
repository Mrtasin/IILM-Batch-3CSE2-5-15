def containsDuplicate(self, nums: List[int]) -> bool:
    m = {}
    for _ in nums:
        if _ in m:
            return True
        m[_] = 1
    return False