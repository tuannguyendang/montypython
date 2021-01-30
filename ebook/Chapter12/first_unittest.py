import unittest


class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        self.assertEqual(1, 1.0)

    def test_str_float(self):
        self.assertEqual(1, "1")

    def test_int_none(self):
        self.assertNotEqual(1, None)


if __name__ == "__main__":
    unittest.main()
