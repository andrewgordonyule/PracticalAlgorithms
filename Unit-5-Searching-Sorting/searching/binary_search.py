# Binary Search
# Takes advantage of ordered list - more efficient than ordered sequential search

# Time complexity: Worst case: O(log n)

# 'Divide and Conquer' approach
def binary_search(list1, val):
    size = len(list1)

    middle = len(list1)//2

    if size == 0:
        return False

    if list1[middle] == val:
        return True

    if(list1[middle] < val):
        binary_search(list1[middle:], val)



def main():


if __name__ == "__main__":
    main()