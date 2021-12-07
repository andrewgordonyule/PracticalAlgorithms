# Binary Search
# Takes advantage of ordered list - more efficient than ordered sequential search
# Time complexity: Worst case: O(log n)

# 'Divide and Conquer' approach
def binary_search(list1, val):
    list_size = len(list1)
    middle = len(list1) // 2

    if list_size == 0:
        return False

    if list1[middle] == val:
        return True

    if val < list1[middle]:
        return binary_search(list1[0:middle], val)
    else:
        return binary_search(list1[middle + 1:list_size], val)


def main():
    my_list = [1, 2, 4, 5, 7, 8, 9]
    target = int(input("Enter value to search for: "))
    found = binary_search(my_list, target)

    print(f"{target} in list: {found}")


def test_binary_search():
    my_list = [1, 2, 4, 5, 7, 8, 9]
    assert (binary_search(my_list, 5) == True), "factorial functional test failed. Unexpected value"
    assert (binary_search(my_list, 3) == False), "factorial functional test failed. Unexpected value"
    assert (binary_search(my_list, 0) == False), "factorial functional test failed. Unexpected value"

    print("binary_search() test: PASS")


if __name__ == "__main__":
    main()
    test_binary_search()
