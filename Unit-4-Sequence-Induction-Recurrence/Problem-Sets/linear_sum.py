# Problem Set - Q2

# Pseudocode
# linear-sum(A, n)
#     if n = 1
#         return A[0]
#     else
#         return linear-sum(A, n-1) + A[n-1]

def linear_sum(A, n):
    print(f"linear_sum called with n = {n}")
    if n == 1:
        return A[0]
    else:
        return linear_sum(A, n - 1) + A[n - 1]


# function for testing, using the "assert" feature.
def test_linear_sum():
    A = [3, 6, 4, 8, 7, 5, 2]
    assert (linear_sum(A, 3) == 13), "linear_sum test failed, unexpected value"

    print("linear_sum() test: PASS")


# run fact test
test_linear_sum()
