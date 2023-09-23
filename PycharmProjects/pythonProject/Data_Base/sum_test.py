import unittest

from Data_Base.Sum import sum_list, list1


class MyTestCase(unittest.TestCase):
    def test_sum(self):
        sum = sum_list(list1,12)
        self.assertEqual(sum, [0, 2])
        # self.assertEqual(sum_list(list1, 12),[0, 2])
        self.assertEqual(sum_list(list1, 16),[2, 3])
        self.assertEqual(sum_list(list1, 15),None)


if __name__ == '__main__':
    unittest.main()
