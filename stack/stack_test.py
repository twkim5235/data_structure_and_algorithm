import unittest
import stack


class TestStack(unittest.TestCase):
    s_stack = stack.Stack()

    print("===== 첫번째 출력 =====")
    s_stack.push(1)
    s_stack.push(2)
    s_stack.push(3)
    s_stack.push(4)

    print(s_stack.pop().data)
    print(s_stack.pop().data)
    print(s_stack.pop().data)
    print(s_stack.pop().data)

    print("===== 두번째 출력 =====")
    s_stack.push(1)
    s_stack.push(2)
    s_stack.push(3)
    s_stack.push(4)
    print(s_stack.peek().data)
    s_stack.pop()
    print(s_stack.peek().data)
    print('is empty: ', s_stack.is_empty())
    s_stack.pop()
    s_stack.pop()
    s_stack.pop()
    print('is empty: ', s_stack.is_empty())
    print(s_stack.pop())