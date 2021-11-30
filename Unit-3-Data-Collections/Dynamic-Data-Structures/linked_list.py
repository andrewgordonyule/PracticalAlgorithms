class NodeSinglyLinkedList:

    def __init__(self, key=0):
        self.key = key
        self.nxt = None

    def get_key(self):
        return self.key

    def set_key(self, key=0):
        self.key = key

    def get_nxt(self):
        return self.nxt

    def set_nxt(self, nxt):
        self.nxt = nxt


# SinglyLinkedList class
class SinglyLinkedList:
    """
    Singly linked list, with head pointer only
    Insertion at the head
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert_head(self, key):
        # create a new node and set key
        node = NodeSinglyLinkedList(key)

        # node inserted at head, so its next should point to where the list head was pointing
        node.nxt = self.head

        # the list's head should now be updated to point at this new node
        self.head = node

    def insert_tail(self):
        print(self[-1])

    def search_key(self, key):
        node = self.head
        while node is not None and node.key != key:
            node = node.nxt
        return node

    def size(self):
        size = 0
        node = self.head
        while node is not None:
            size += 1
            node = node.nxt

        return size

    def print_all_keys(self):
        node = self.head
        while node is not None:
            print(node.key)
            node = node.nxt


# Test SinglyLinkedList
# =============================================================================
ll = SinglyLinkedList()
ll.empty()
ll.insert_head(1)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
ll.empty()
ll.print_all_keys()
print('The size is: ', ll.size())
if ll.search_key(3): print("Found key")
if ll.search_key(13): print("Found key")
# =============================================================================
