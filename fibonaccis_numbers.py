# --- Fibonacci's Numbers --- #

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

num = int(input("Pick a number: "))
for n in range(1, (num + 1)): 
    print(n, "->", fib(n))


# --- Non-Recursive --- #

# def fib(n):
#     if n < 1:
#          return None
#     if n < 3:
#         return 1

#     e1 = e2 = 1
#     sum = 0
    
#     for i in range(3, n + 1):
#         sum = e1 + e2
#         e1, e2 = e2, sum
#     return sum

# num = int(input("Pick a number: "))
# for n in range(1, (num + 1)): 
#     print(n, "-->", fib(n))