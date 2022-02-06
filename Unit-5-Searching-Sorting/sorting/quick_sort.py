# Quick Sort Algorithm

# Time Complexity
# Best Case: O(n log n)
# Worst Case: O(n^2)

def partition(arr, start, end):
    pivot = end
    x = arr[pivot]
    lrbi = start - 1
    for ti in range(start, end):
        if arr[ti] <= x:
            lrbi += 1
            arr[ti], arr[lrbi] = arr[lrbi], arr[ti]
    arr[lrbi + 1], arr[pivot] = arr[pivot], arr[lrbi + 1]
    return lrbi + 1


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)


if __name__ == "__main__":
    myNumbers = [5, 3, 7, 1, 4, 2, 9, 6, 8, 0]
    print("Unsorted:\t", myNumbers)
    quick_sort(myNumbers, 0, len(myNumbers)-1)
    print("Sorted:\t\t", myNumbers)
