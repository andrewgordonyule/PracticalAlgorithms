# Merge Sort Algorithm
import sys

# Time Complexity: O(n log n)

def merge(arr, start, mid, end):
    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]

    left.append(sys.maxsize)
    right.append(sys.maxsize)

    left_index = 0
    right_index = 0

    for top_index in range(start, end + 1):
        if left[left_index] < right[right_index]:
            arr[top_index] = left[left_index]
            left_index += 1
        else:
            arr[top_index] = right[right_index]
            right_index += 1


def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


if __name__ == "__main__":
    myNumbers = [5, 3, 7, 1, 4, 2, 9, 6, 0, 8]
    print("Unsorted:\t", myNumbers)

    size = len(myNumbers)
    merge_sort(myNumbers, 0, size - 1)
    print("Sorted:\t\t", myNumbers)
