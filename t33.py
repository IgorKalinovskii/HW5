import unittest

def triangleType(a,b,c):
    if not ((a + b) > c and (a + c) > b and (b + c) > a):
        return 'Not a triangle'
    elif a == b == c:
        return 'Equilateral triangle'
    elif a == b or a == c or b == c:
        return 'Isosceles triangle'
    else:
        return 'Versatile triangle'

class TestTriangleType(unittest.TestCase):
    def testTriangleTypeNotATriangle(self):
        res = triangleType(1, 1, 4)
        self.assertEqual(res, 'Not a triangle')

    def testTriangleTypeEquailateral(self):
        res = triangleType(7, 7, 7)
        self.assertEqual(res, 'Equilateral triangle')

    def testTriangleTypeIsosceles(self):
        res = triangleType(7, 7, 5)
        self.assertEqual(res, 'Isosceles triangle')

    def testTriangleTypeVersatile(self):
        res = triangleType(3, 4, 5)
        self.assertEqual(res, 'Versatile triangle')


if __name__ == '__main__':
    unittest.main()
