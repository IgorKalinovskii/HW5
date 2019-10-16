import unittest


def isatriangle(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        return True
    else:
        return False

class TestTriangle(unittest.TestCase):

    def testisATriangleWorksForATriangle(self):  #  работает для заведомо треугольника
        res = isatriangle(3, 4, 5)
        self.assertTrue(res)

    def testisATriangleDoesntWorkForNotATriangle(self):  # не работает для заведомо не треугольника
        res = isatriangle(1, 1, 4)
        self.assertFalse(res)
        res = isatriangle(1, 4, 1)   # так вообще можно делать? или дурной тон? По паре штук ассертов в функции.
        self.assertFalse(res)       # мне кажется в этом случае уместо, т.к. проверяется один и тот же кейс
        res = isatriangle(1, 1, 4)
        self.assertFalse(res)

    def testisATriangleStrictlyMore(self):  # проверяет что именно больше а не >=
        res = isatriangle(0.5, 0.5, 1)
        self.assertFalse(res)
        res = isatriangle(1, 0.5, 0.5)
        self.assertFalse(res)
        res = isatriangle(0.5, 1, 0.5)
        self.assertFalse(res)

    def testIsATriangleAllZeroes(self):
        res = isatriangle(0, 0, 0)
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
