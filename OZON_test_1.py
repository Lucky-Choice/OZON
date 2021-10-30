import unittest

# класс MyTest унаследован от unittest.TestCase 
# тестовую ф-ю def test_first внутри класса MyTest которая в качестве аргумента принимает self
class MyTest(unittest.TestCase):
    def test_first(self):
        sum_ = 2+2
        assert sum_ == 4


if __name__ == '__main__':
    unittest.main()
