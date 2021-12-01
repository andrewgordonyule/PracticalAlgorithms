# Reverse Array using tail recursion

def reverse_array(A, i, j):
    print(f"reverse_array where i = {i}, j = {j}")
    if i < j:
        swap(A, i, j)
        reverse_array(A, i + 1, j - 1)


def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def test_reverse_array():
    A = [3, 6, 4, 8, 7, 5, 2]
    reverse_array(A, 0, len(A) - 1)  # note that reverse_array changes A in-place
    assert (A == [2, 5, 7, 8, 4, 6, 3]), "reverse_array functional test failed. Unexpected value"

    print("reverse_array() test: PASS")


test_reverse_array()
