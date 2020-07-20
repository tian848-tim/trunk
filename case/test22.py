import unittest
import requests

class TestA(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        self.g = globals()

    def test_a(self):
        '''用例a'''
        result_a = "aaaaaa"    # 用例a的返回值

        # 返回值先给全部办理，存到字典对应key
        self.g["a"] = result_a
        self.assertEqual(result_a, "aaaaaa")

        print(self.g["a"])

    def test_b(self):
        '''用例b'''
        b = self.g["a"]  # 引用用例a的返回值
        print("用例b引用用例a的返回值：%s"%b)
        result_b = b+"111"
        self.g["b"] = result_b
        self.assertEqual(result_b, "aaaaaa111")

    def test_c(self):
        '''用例c'''
        print("用例c依赖用例a和用例b")

        c_a = self.g["a"]
        c_b = self.g["b"]
        print("用例c的请求入参：%s" % c_a)
        print("用例c的请求入参：%s" % c_b)

if __name__ == '__main__':
    unittest.main()