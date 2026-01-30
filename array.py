l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [[9,8,7],[6,5,4],[3,2,1]]

result = []

x = 0
while x < len(l1):
    z = 0
    ans = []
    while z < len(l1[x]):
        ans.append(l1[x][z] + l2[x][z])
        z += 1
    result.append(ans)
    x += 1

for v in result:
    for data in v:
        print(data, end=" ")
    print()