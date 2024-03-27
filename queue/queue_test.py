import unittest
import queue


class TestQueue(unittest.TestCase):
    v_queue = queue.Queue()

    print("======== enqueue() 세번 호출 ========")
    v_queue.enqueue(1)
    v_queue.enqueue(2)
    v_queue.enqueue(3)

    print(v_queue.front().data)

    print("======== dequeue() 네번 호출 ========")
    print(v_queue.dequeue().data)
    print(v_queue.dequeue().data)
    print(v_queue.dequeue().data)
    print(v_queue.dequeue())

    print("is_empty: ",v_queue.is_empty())
