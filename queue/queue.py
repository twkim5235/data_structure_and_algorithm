import dobule_linked_list.doubly_linked_list as dll


class Queue:
    def __init__(self):
        self.list = dll.DoublyLinkedList()

    def enqueue(self, data):
        self.list.insert_at(0, data)

    def dequeue(self):
        try:
            return self.list.delete_last_node()
        except IndexError:
            return None

    def front(self):
        return self.list.tail

    def is_empty(self):
        return self.list.count == 0
