# Recursive Fibonnaci Method

def Fibonacci(n):
    if n<2:
        return 0
    if n<3:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

# Calculation example

print(Fibonacci(10)) # 34
