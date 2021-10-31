import unittest

# класс MyTest унаследован от unittest.TestCase 
# тестовую ф-ю def test_first внутри класса MyTest которая в качестве аргумента принимает self
# self.assertEqual Функция, которая в ответет выводит не равное значение
# test_second вывод конкретной функции через папки python3 -m unittest OZON_test_1.MyTest.test_second -v
class MyTest(unittest.TestCase):
    def test_first(self):
        sum_ = 2+2
        assert sum_ == 4

    def test_second(self):
        sum_ = 2 + 2
        assert sum_ == 4    


if __name__ == '__main__':
    unittest.main()
