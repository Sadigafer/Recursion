# Recursive factorial

def Factorial(n):
    if n<2:
        return 1
    else:
        return n* Factorial(n-1)

# Calculation example

print(Factorial(5)) # 120