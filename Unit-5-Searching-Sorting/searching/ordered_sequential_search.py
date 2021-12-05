# Ordered sequential search

# If list is ordered, no need to continue sequence if val at index > val
def ordered_sequential_search(list1, val):
    for i in range(len(list1)):
        if list1[i] == val:
            return True
        if list1[i] > val:
            return False
    return False


def main():
    my_list = [1, 2, 4, 6, 7, 9]
    found = ordered_sequential_search(my_list, 7)
    print("Value found:", found)


if __name__ == "__main__":
    main()
