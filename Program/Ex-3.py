def factorial_iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
n = 5
print("Iterative Factorial:", factorial_iterative(n))
print("Recursive Factorial:", factorial_recursive(n))
