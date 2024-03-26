import linked_list.linked_list as ll


class Stack:
    list = ll.LinkedList()

    def push(self, data):
        self.list.insert_at(0, data)

    def pop(self):
        try:
            return self.list.delete_at(0)

        except Exception as e:
            return None

    def peek(self):
        return self.list.get_node_at(0)

    def is_empty(self) -> bool:
        return self.list.count == 0
