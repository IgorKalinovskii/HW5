import unittest


def vys(x):
    x = int(x)
    if (x%4==0 and x%100 != 0) or x%400 == 0:
        return True
    else:
        return False


class TestYear(unittest.TestCase):
    def test_vys_year_assert_true(self): # random vys year
        res = vys(1904)
        self.assertTrue(res)

    def test_not_vys_year(self): # random NOT vys year
        res = vys(2019)
        self.assertFalse(res)

    # def test_vys_year_mod4(self):  # x%4==0
    #     res = vys(2244)
    #     self.assertTrue(res)
    #
    # def test_vys_year_mod100_not_zero(self):  #x%100 != 0
    #     res = vys(2016)
    #     self.assertTrue(res)

    def test_vys_year_mod4_and_mod100_not_zero(self):  # x%4==0 AND x%100 != 0
        res = vys(2016)
        self.assertTrue(res)

    def test_vys_year_mod4_and_NOT_mod100_not_zero(self):  # x%4==0 but NOT x%100 != 0
        res = vys(1900)
        self.assertFalse(res)

    def test_vys_year_NOT_mod4_and_mod100_not_zero(self):  # NOT x%4==0 but x%100 != 0
        res = vys(1999)
        self.assertFalse(res)

    def test_vys_year_mod400(self):  # x%400 == 0
        res = vys(2400)
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
