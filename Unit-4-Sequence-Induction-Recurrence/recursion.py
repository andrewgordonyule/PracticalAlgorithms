# Classic recursion example
# Rule 1: Size of data set must be reduced on each recursive call
# Rule 2: There must be a terminating condition

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Enter number: "))
result = factorial(number)
print(f"The factorial of {number} is:", result)
