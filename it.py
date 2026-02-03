s1 = {1,2,3,4,5,6,7,8,9,10}
it = iter(s1)
while True:
    try:
        data = next(it)
        print(data, end=' ')
    except StopIteration as e:
        break
