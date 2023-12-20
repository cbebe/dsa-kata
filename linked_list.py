import fem_list


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(fem_list.List):
    def __init__(self):
        self.head = None

    def prepend(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_at(self, item, idx):
        if idx == 0:
            self.prepend(item)
            return
        node = self.head
        total = 0
        while node and total + 1 != idx:
            total += 1
            node = node.next
        if not node:
            return None
        i = Node(item)
        i.next = node.next
        node.next = i

    def append(self, item):
        i = Node(item)
        node = self.head
        if node is None:
            self.head = i
        else:
            while node.next:
                node = node.next
            node.next = i

    def remove(self, item):
        node = self.head
        # This is the only element
        if node and node.val == item:
            self.head = node.next
            return node.val
        while node and node.next and node.next.val != item:
            node = node.next
        # Out of bounds or not found
        if ((not node)
                or (not node.next)
                or (node.next and node.next.val != item)):
            return None
        ret = node.next
        node.next = ret.next
        return ret.val

    def get(self, idx):
        node = self.head
        total = 0
        while node and total != idx:
            total += 1
            node = node.next
        return node.val

    def remove_at(self, idx):
        node = self.head
        if idx == 0:
            self.head = node.next
            return node.val
        total = 0
        while node and total + 1 != idx:
            total += 1
            node = node.next
        # Out of bounds or not found
        if not node:
            return None
        ret = node.next
        node.next = ret.next
        return ret.val

    @property
    def length(self):
        node = self.head
        total = 0
        while node:
            total += 1
            node = node.next
        return total

    def __str__(self):
        s = "["
        node = self.head
        while node:
            s += str(node.val)
            node = node.next
            if node:
                s += ", "

        return s + "]"


if __name__ == "__main__":
    ll = LinkedList()
    fem_list.test_list(ll)
    print("OK")
