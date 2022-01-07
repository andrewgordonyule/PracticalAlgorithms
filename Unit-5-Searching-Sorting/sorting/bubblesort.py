# Bubble Sort Algorithm

# Time Complexity: O(n^2)
def bubblesort(arr):
    n = len(arr)
    for outer in range(n - 1, 0, -1):
        for i in range(outer):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


if __name__ == "__main__":
    myNumbers = [5, 3, 7, 1, 4, 2, 9, 6, 8, 0]

    print("Unsorted:\t", myNumbers)

    bubblesort(myNumbers)

    print("Sorted:\t\t", myNumbers)
