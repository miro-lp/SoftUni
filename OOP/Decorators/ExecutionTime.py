from timeit import default_timer as timer


def exec_time(func):
    def wrapper(*args):
        star_time = timer()
        func(*args)
        end_time = timer()
        return end_time - star_time

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))

@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))

# test first zero
# import unittest
# import time
#
# class ExecTimeTests(unittest.TestCase):
#     def test_zero_first(self):
#         @exec_time
#         def loop(start, end):
#             total = 0
#             for x in range(start, end):
#                 total += x
#             return total
#         self.assertEqual(round(loop(1, 10000000)), 1)
#
# if __name__ == '__main__':
#     unittest.main()

# test second zero
import unittest
import time

class ExecTimeTests(unittest.TestCase):
    def test_zero_second(self):
        @exec_time
        def concatenate(strings):
            result = ""
            for string in strings:
                result += string
            return result
        self.assertEqual(round(concatenate(["a" for i in range(1000000)])), 0)

if __name__ == '__main__':
    unittest.main()