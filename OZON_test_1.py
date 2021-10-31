import unittest
# from hamcrest import assert_that, equal_to - не находит модуль
# класс MyTest унаследован от unittest.TestCase 
# тестовую ф-ю def test_first внутри класса MyTest которая в качестве аргумента принимает self
# self.assertEqual Функция, которая в ответет выводит не равное значение
# test_second вывод конкретной функции через папки python3 -m unittest OZON_test_1.MyTest.test_second -v
# setUp - перед запуском теста выводит слово  start test
# tearDown - после теста выводит слово  finish
# @classmethod - обявили метод класса
class MyTest(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        print("Before all")

    @classmethod
    def tearDownClass(cls):
        print("After all")    

    def setUp(self):
        print("start test")

    def tearDown(self):
        print("finish")

    def test_first(self):
        print("one")
        sum_ = 2+2
        assert sum_ == 4

    def test_second(self):
        print("tow")
        sum_ = 2 + 2
        assert sum_ == 4    


# if __name__ == '__main__':
#   unittest.main()
