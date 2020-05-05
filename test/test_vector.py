
import unittest
from generalvector.vector import Vec

class VecTest(unittest.TestCase):
    def test_vec(self):
        self.assertRaises(TypeError, Vec, "")
        self.assertRaises(TypeError, Vec, 5, 2, "")
        self.assertRaises(TypeError, Vec, 5, "", 2)

        self.assertRaises(AttributeError, Vec, None, 5)
        self.assertRaises(AttributeError, Vec, 2, 5)

        self.assertEqual(Vec(5, 2, 1).x, 5)
        self.assertEqual(Vec(5, 2, 1).y, 2)
        self.assertEqual(Vec(5, 2, 1).z, 1)

        self.assertEqual(Vec(5.2, 2.5, 1.4).x, 5.2)
        self.assertEqual(Vec(5.2, 2.5, 1.4).y, 2.5)
        self.assertEqual(Vec(5.2, 2.5, 1.4).z, 1.4)

        self.assertEqual(Vec(5).x, 5)
        self.assertEqual(Vec(5).y, 5)
        self.assertEqual(Vec(5).z, 5)

    def test_equal(self):
        self.assertRaises(TypeError, Vec.__eq__, "")

        self.assertTrue(Vec(1) == Vec(1))
        self.assertTrue(Vec(1, 2, 3) == Vec(1, 2, 3))
        self.assertTrue(Vec(1, 1, 1) == 1)
        self.assertTrue(Vec(5.2, 5.2, 5.2) == 5.2)

        self.assertFalse(Vec(1, 2, 3) == Vec(1, 3, 3))
        self.assertFalse(Vec(1, 2, 3) == Vec(2, 2, 3))

        self.assertFalse(Vec(1, 1, 3) == 2)
        self.assertFalse(Vec(5.2, 5.2, 3) == 5)

    def test_add(self):
        self.assertRaises(TypeError, Vec.__add__, "")
        self.assertRaises(TypeError, Vec.__add__, False)

        self.assertEqual(Vec(5, 2, 3) + Vec(2, 4, 3), Vec(7, 6, 6))
        self.assertEqual(Vec(5, 2, 3) + Vec(2.5, 4.5, 3.5), Vec(7.5, 6.5, 6.5))
        self.assertEqual(Vec(5, 2, 3) + Vec(-2, -4, -3), Vec(3, -2, 0))

        self.assertEqual(Vec(5, 2, 3) + 3, Vec(8, 5, 6))
        self.assertEqual(Vec(5, 2, 3) + -3, Vec(2, -1, 0))
        self.assertEqual(Vec(5, 2, 3) + 3.5, Vec(8.5, 5.5, 6.5))

    def test_sub(self):
        self.assertRaises(TypeError, Vec.__sub__, "")
        self.assertRaises(TypeError, Vec.__sub__, True)

        self.assertEqual(Vec(5, 2, 3) - Vec(2, 4, 3), Vec(3, -2, 0))
        self.assertEqual(Vec(5, 2, 3) - Vec(-2, -4, -3), Vec(7, 6, 6))
        self.assertEqual(Vec(5, 2, 3) - 3, Vec(2, -1, 0))
        self.assertEqual(Vec(5, 2, 3) - -3, Vec(8, 5, 6))
        self.assertEqual(Vec(5, 2, 3) - 3.5, Vec(1.5, -1.5, -0.5))

    def test_mul(self):
        self.assertRaises(TypeError, Vec.__mul__, "")
        self.assertRaises(TypeError, Vec.__mul__, True)
        self.assertRaises(NotImplementedError, Vec(5, 2, 3).__mul__, Vec(5, 2, 3))

        self.assertEqual(Vec(5, 2, 3) * 2, Vec(10, 4, 6))
        self.assertEqual(Vec(5, 2, 3) * 2.5, Vec(12.5, 5, 7.5))

    def test_div(self):
        self.assertRaises(TypeError, Vec.__truediv__, "")
        self.assertRaises(TypeError, Vec.__truediv__, False)
        self.assertRaises(NotImplementedError, Vec(5, 2, 3).__truediv__, Vec(5, 2, 3))

        self.assertEqual(Vec(5, 2, 3) / 2, Vec(2.5, 1, 1.5))
        self.assertEqual(Vec(10, 5, 7.5) / 2.5, Vec(4, 2, 3))

    def test_length(self):
        self.assertEqual(Vec(10, 0, 0).length(), 10)
        self.assertEqual(Vec(0, 10, 0).length(), 10)
        self.assertEqual(Vec(0, 0, 10).length(), 10)
        self.assertEqual(Vec(0, 0.2, 0).length(), 0.2)
        self.assertEqual(Vec(0, 0, 0).length(), 0)

    def test_normalized(self):
        self.assertEqual(Vec(10, 0, 0).normalized(), Vec(1, 0, 0))
        self.assertEqual(Vec(0, 10, 0).normalized(), Vec(0, 1, 0))
        self.assertEqual(Vec(0, 0.2, 0).normalized(), Vec(0, 1, 0))
        self.assertEqual(Vec(0, 0, 0).normalized(), Vec(0, 0, 0))
        self.assertEqual(Vec(0, -10, 0).normalized(), Vec(0, -1, 0))

