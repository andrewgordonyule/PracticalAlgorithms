# Insertion Sort Algorithm

# Time Complexity:
# Worst Case O(n^2)
# Best Case: O(n)
def insertion_sort(arr):

    n = len(arr)

    for outer in range(1, n):
        key = arr[outer]
        inner = outer

        while inner > 0 and arr[inner - 1] > key:
            arr[inner] = arr[inner - 1]
            inner -= 1

        arr[inner] = key


if __name__ == "__main__":
    myNumbers = [5, 3, 7, 1, 4, 2, 9, 6, 8, 0]
    print("Unsorted:\t", myNumbers)
    insertion_sort(myNumbers)
    print("Sorted:\t\t", myNumbers)