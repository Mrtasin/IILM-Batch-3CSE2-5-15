# import functools
from functools import reduce
l1 = [1,2,3,4,5,6,7,8,9,10]

# ans = list(map(lambda a: a*a, l1))
# ans = map(lambda a: a*a, l1)

# for v in ans:
#     print(v,end=" ")

# print(ans)

# ans = reduce(lambda a,b:a*b, l1)

# print(ans)

ans = list(filter(lambda a: not(a % 2) ,l1))

print(ans)