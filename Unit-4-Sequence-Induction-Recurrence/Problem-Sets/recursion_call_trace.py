# Problem Set
# Call trace - graphical method to visualise execution of recursive algorithm

def factorial(n):
    print(f"Inside factorial() where n = {n}")
    if n == 1:
        print("return: 1")
        return 1
    else:
        return n * factorial(n - 1)


# function for testing factorial, using the "assert" feature.
def test_factorial():
    assert (factorial(5) == 120), "factorial functional test failed. Unexpected value"
    assert (factorial(8) == 40320), "factorial functional test failed. Unexpected value"
    assert (factorial(10) == 3628800), "factorial functional test failed. Unexpected value"

    print("factorial() test: PASS")


# run fact test
test_factorial()
