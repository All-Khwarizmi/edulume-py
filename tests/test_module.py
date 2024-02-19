import unittest


class TestModule(unittest.TestCase):
    def test_module(self):
        self.assertTrue(True)

    def test_module2(self):
        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()
