import unittest
# from hamcrest import assert_that, equal_to - не находит модуль
# класс MyTest унаследован от unittest.TestCase 
# тестовую ф-ю def test_first внутри класса MyTest которая в качестве аргумента принимает self
# self.assertEqual Функция, которая в ответет выводит не равное значение
# test_second вывод конкретной функции через папки python3 -m unittest OZON_test_1.MyTest.test_second -v
# setUp - перед запуском теста выводит слово  start test
# tearDown - после теста выводит слово  finish
# @classmethod - обявили метод класса

# Декораторы 
# @unittest.skip("New feature CB-15777") - не поддерживается
# @unittest.skipIf(Versoin > 0.9, "not supported") - не поддерживается при условии
# @unittest.expectedFailure - тест не работает и мы об этом знаем(ожидаемые сбои)
class MyTest(unittest.TestCase): 
    Versoin = 1.0
    
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
        sum_ = 2 + 1
        assert sum_ == 3

    def test_second(self):
        print("two")
        sum_ = 2 + 2
        assert sum_ == 4    

    @unittest.skip("New feature CB-15777")
    def test_third(self):
        print("third")
        sum_ = 2 + 3
        assert sum_ == 5   
        
    @unittest.skipIf(Versoin > 0.9, "not supported")
    def test_fourth(self):
        print("fourth")
        sum_ = 2 + 5
        assert sum_ == 7     

    @unittest.expectedFailure
    def test_fifth(self):
        print("fifth")
        sum_ = 2 + 2
        assert sum_ == 8  

    # # параметромизация
    # def test_sixth(self):
    #     for i in range(1,6):
    #         with self.subTest(i=i):
    #             self.assertGreater(i,0)





# if __name__ == '__main__':
#   unittest.main()
