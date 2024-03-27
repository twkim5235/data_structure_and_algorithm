class Node:
    data = 0
    next_node = None
    prev_node = None

    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert_at(self, index, data):
        if index > self.count or index < 0:
            raise Exception('Index out of range')

        new_node = Node(data)
        if index == 0:
            new_node.next_node = self.head

            if self.head is not None:
                self.head.prev_node = new_node

            self.head = new_node
        elif index == self.count:
            new_node.next_node = None
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
        else:
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next_node

            new_node.next_node = current_node.next_node
            new_node.prev_node = current_node
            current_node.next_node = new_node
            new_node.next_node.prev_node = new_node

        if new_node.next_node is None:
            self.tail = new_node

        self.count += 1

    def print_all(self):
        current_node = self.head
        text = '['

        while current_node is not None:
            text += str(current_node.data)
            current_node = current_node.next_node

            if current_node is not None:
                text += ', '

        text += ']'
        print(text)

    def clear(self):
        self.head = None
        self.count = 0

    def insert_last(self, data):
        self.insert_at(self.count, data)

    def delete_at(self, index):
        if index < 0 or index > self.count:
            raise IndexError('Index out of range')

        current_node = self.head

        if index == 0:
            deleted_node = self.head
            if self.head.next_node is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next_node
                self.head.prev_node = None
            self.head = deleted_node.next_node
            self.count -= 1
            return deleted_node
        elif index == self.count - 1:
            deleted_node = self.tail
            self.tail.prev_node.next_node = None
            self.tail = self.tail.prev_node
            self.count -= 1
            return deleted_node
        else:
            for i in range(index - 1):
                current_node = current_node.next_node

            deleted_node = current_node.next_node
            current_node.next_node = deleted_node.next_node
            current_node.next_node.prev_node = current_node
            self.count -= 1
            return deleted_node

    def delete_last_node(self):
        return self.delete_at(self.count - 1)

    def get_node_at(self, index):
        if index < 0 or index > self.count:
            raise Exception('Index out of range')

        current_node = self.head
        for i in range(index):
            current_node = current_node.next_node

        return current_node
