class Node:
    data = 0
    next_node = None

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert_at(self, index, data):
        if index > self.count or index < 0:
            raise Exception('Index out of range')

        new_node = Node(data)
        if index == 0:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next_node

            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

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
            raise Exception('Index out of range')

        if index == 0:
            deleted_node = self.head
            self.head = deleted_node.next_node
            self.count -= 1
            return deleted_node
        else:
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next_node

            deleted_node = current_node.next_node
            current_node.next_node = deleted_node.next_node
            self.count -= 1
            return deleted_node

    def delete_last_node(self):
        self.delete_at(self.count - 1)

    def get_node_at(self, index):
        if index < 0 or index > self.count:
            raise Exception('Index out of range')

        current_node = self.head
        for i in range(index):
            current_node = current_node.next_node

        return current_node
