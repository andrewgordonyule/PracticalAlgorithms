# Example from Summations lecture
# Solving Recurrence Relations

# The sum of the first n positive integers
# Σ i = 1 + 2 + 3 + ... + n-1 + n

# Iterative approach
# Time complexity = O(n)
n = int(input("Enter value of n to sum: "))
total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print(f"Sum of first {n} numbers is:", total_sum)

# Using Closed Form
# Time complexity O(1)
summation = n * (n + 1) // 2
print(f"Sum of first {n} numbers is:", summation)

