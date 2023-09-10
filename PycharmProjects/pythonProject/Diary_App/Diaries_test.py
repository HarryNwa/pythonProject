import unittest

from Diary_App.Diaries import Diaries


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.diaries = Diaries()

    def test_that_diaries_exists(self):
        self.assertIsNotNone(self.diaries)


if __name__ == '__main__':
    unittest.main()
