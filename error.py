try :
    num = int(input("Enter a number : "))
    c = 10 / num
    
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("Tasin Coder")