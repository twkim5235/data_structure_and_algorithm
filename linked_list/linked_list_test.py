import linked_list
import unittest


class LinkedListTest(unittest.TestCase):
    node1 = linked_list.Node(1)
    node2 = linked_list.Node(2)
    node3 = linked_list.Node(3)

    node1.next_node = node2
    node2.next_node = node3

    print(node1.data)
    print(node1.next_node.data)
    print(node1.next_node.next_node.data)

    l_list = linked_list.LinkedList()

    print("======= insertAt() 다섯번 호출=======")
    l_list.insert_at( 0, 0)
    l_list.insert_at(1, 1)
    l_list.insert_at(2, 2)
    l_list.insert_at(3, 3)
    l_list.insert_at(4, 4)
    l_list.print_all()

    print("======= clear() 호출 =========")
    l_list.clear()
    l_list.print_all()

    print("======= insert_last() 호출 ========")
    l_list.insert_last(0)
    l_list.insert_last(1)
    l_list.insert_last(2)
    l_list.print_all()

    print("======== delete_at() 호출 ========")
    l_list.delete_at(0)
    l_list.print_all()
    l_list.delete_at(1)
    l_list.print_all()

    print("======== delete_last() 호출 ========")
    l_list.insert_last(5)
    # l_list.delete_last_node()
    l_list.delete_last_node()
    l_list.delete_last_node()
    l_list.print_all()

    print("======== get_node_at() 호출 ========")
    l_list.insert_last(1)
    l_list.insert_last(2)
    l_list.insert_last(3)
    l_list.insert_last(4)
    l_list.insert_last(5)

    second_node = l_list.get_node_at(2)
    print(second_node.data)
