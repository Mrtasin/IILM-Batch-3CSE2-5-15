add  = lambda a,b: a+b

fact = lambda n : n * fact(n-1) if n > 0 else 1

print(fact(6))

