num = [1,2,3,4,5,4,3,2,1]

start = 0
end = len(num) - 1

while start <= end:
    if(num[start] != num[end]):
        print("Not Palindrome list")
        break
    start += 1
    end -= 1
else:
    print("Palindrome List")