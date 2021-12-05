# Sequential search

# Time Complexity:
# If item is present: Best Case = Ω(1), Worst Case = O(n)
# If item not present: Best Case = Ω(n), Worst Case = O(n)

def sequential_search(list1, val):
    for i in range(len(list1)):
        if list1[i] == val:
            return True
    return False


def main():
    my_list = [3, 5, 7, 1, 2]
    found = sequential_search(my_list, 7)
    print("Value found:", found)


if __name__ == "__main__":
    main()
