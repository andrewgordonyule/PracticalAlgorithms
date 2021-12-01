# Factorial with tail recursion

def test_fact(func2test):
    assert (func2test(5) == 120), "FACT functional test failed. Unexpected value"
    assert (func2test(8) == 40320), "FACT functional test failed. Unexpected value"
    assert (func2test(10) == 3628800), "FACT functional test failed. Unexpected value"

    print("function test: PASS")


def fact_iter(n):
    acc = 1
    while n != 1:
        acc = n * acc
        n -= 1
    return acc


def fact_tail(n, acc=1):
    if n == 1:
        return acc
    else:
        acc = n * acc
        return fact_tail(n - 1, acc)


# run tests
test_fact(fact_tail)

test_fact(fact_iter)

