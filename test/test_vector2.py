
import unittest
from generalvector.vector2 import Vec2

class Vec2Test(unittest.TestCase):
    def test_vec2(self):
        self.assertRaises(TypeError, Vec2, "")
        self.assertRaises(TypeError, Vec2, None, 5)

        self.assertEqual(Vec2(5, 2).x, 5)
        self.assertEqual(Vec2(5, 2).y, 2)
        self.assertEqual(Vec2(5.2, 2).x, 5.2)
        self.assertEqual(Vec2(5.2, 2.5).y, 2.5)
        self.assertEqual(Vec2(5).x, 5)
        self.assertEqual(Vec2(5).y, 5)

        self.assertEqual(Vec2(5, 2), Vec2(Vec2(5, 2)))

    def test_equal(self):
        self.assertRaises(TypeError, Vec2.__eq__, "")

        self.assertTrue(Vec2(1) == Vec2(1))
        self.assertTrue(Vec2(1, 2) == Vec2(1, 2))
        self.assertTrue(Vec2(1, 1) == 1)
        self.assertTrue(Vec2(5.2, 5.2) == 5.2)

        self.assertFalse(Vec2(1, 2) == Vec2(1, 3))
        self.assertFalse(Vec2(1, 2) == Vec2(2, 2))
        self.assertFalse(Vec2(1, 1) == 2)
        self.assertFalse(Vec2(5.2, 5.2) == 5)

    def test_add(self):
        self.assertRaises(TypeError, Vec2.__add__, "")
        self.assertRaises(TypeError, Vec2.__add__, False)


        self.assertEqual(Vec2(5, 2) + Vec2(2, 4), Vec2(7, 6))
        self.assertEqual(Vec2(5, 2) + Vec2(2.5, 4.5), Vec2(7.5, 6.5))
        self.assertEqual(Vec2(5, 2) + Vec2(-2, -4), Vec2(3, -2))
        self.assertEqual(Vec2(5, 2) + 3, Vec2(8, 5))
        self.assertEqual(Vec2(5, 2) + -3, Vec2(2, -1))
        self.assertEqual(Vec2(5, 2) + 3.5, Vec2(8.5, 5.5))

    def test_sub(self):
        self.assertRaises(TypeError, Vec2.__sub__, "")
        self.assertRaises(TypeError, Vec2.__sub__, True)

        self.assertEqual(Vec2(5, 2) - Vec2(2, 4), Vec2(3, -2))
        self.assertEqual(Vec2(5, 2) - Vec2(-2, -4), Vec2(7, 6))
        self.assertEqual(Vec2(5, 2) - 3, Vec2(2, -1))
        self.assertEqual(Vec2(5, 2) - -3, Vec2(8, 5))
        self.assertEqual(Vec2(5, 2) - 3.5, Vec2(1.5, -1.5))

    def test_mul(self):
        self.assertRaises(TypeError, Vec2.__mul__, "")
        self.assertRaises(TypeError, Vec2.__mul__, True)

        self.assertEqual(Vec2(5, 2) * 2, Vec2(10, 4))
        self.assertEqual(Vec2(5, 2) * 2.5, Vec2(12.5, 5))

        self.assertEqual(Vec2(5, 2) * Vec2(2, 1), Vec2(10, 2))

    def test_div(self):
        self.assertRaises(TypeError, Vec2.__truediv__, "")
        self.assertRaises(TypeError, Vec2.__truediv__, False)

        self.assertEqual(Vec2(5, 2) / 2, Vec2(2.5, 1))
        self.assertEqual(Vec2(10, 5) / 2.5, Vec2(4, 2))

        self.assertEqual(Vec2(10, 5) / Vec2(5, 2), Vec2(2, 2.5))

    def test_length(self):
        self.assertEqual(Vec2(10, 0).length(), 10)
        self.assertEqual(Vec2(0, 10).length(), 10)
        self.assertEqual(Vec2(0, 0.2).length(), 0.2)
        self.assertEqual(Vec2(0, 0).length(), 0)

    def test_normalized(self):
        self.assertEqual(Vec2(10, 0).normalized(), Vec2(1, 0))
        self.assertEqual(Vec2(0, 10).normalized(), Vec2(0, 1))
        self.assertEqual(Vec2(0, 0.2).normalized(), Vec2(0, 1))
        self.assertEqual(Vec2(0, 0).normalized(), Vec2(0, 0))
        self.assertEqual(Vec2(0, -10).normalized(), Vec2(0, -1))

    def test_round(self):
        self.assertEqual(Vec2(5, 2), Vec2(5.3, 1.5).round())

    def test_random(self):
        randvec = Vec2.random(5)
        self.assertGreaterEqual(randvec.x, 0)
        self.assertGreaterEqual(randvec.y, 0)
        self.assertLessEqual(randvec.x, 5)
        self.assertLessEqual(randvec.y, 5)

        randvec = Vec2.random(3, 5)
        self.assertGreaterEqual(randvec.x, 3)
        self.assertGreaterEqual(randvec.y, 3)
        self.assertLessEqual(randvec.x, 5)
        self.assertLessEqual(randvec.y, 5)

        randvec = Vec2.random(Vec2(-1, 2))
        self.assertGreaterEqual(randvec.x, -1)
        self.assertGreaterEqual(randvec.y, 0)
        self.assertLessEqual(randvec.x, 0)
        self.assertLessEqual(randvec.y, 2)

        randvec = Vec2.random(Vec2(4, 2), 8)
        self.assertGreaterEqual(randvec.x, 4)
        self.assertGreaterEqual(randvec.y, 2)
        self.assertLessEqual(randvec.x, 8)
        self.assertLessEqual(randvec.y, 8)

        randvec = Vec2.random(8, Vec2(4, 2))
        self.assertGreaterEqual(randvec.x, 4)
        self.assertGreaterEqual(randvec.y, 2)
        self.assertLessEqual(randvec.x, 8)
        self.assertLessEqual(randvec.y, 8)

        randvec = Vec2.random(Vec2(3.5, 3), Vec2(4, 2))
        self.assertGreaterEqual(randvec.x, 3.5)
        self.assertGreaterEqual(randvec.y, 2)
        self.assertLessEqual(randvec.x, 4)
        self.assertLessEqual(randvec.y, 3)

    def test_min(self):
        self.assertEqual(Vec2(5, 2), Vec2(8, 2).min(Vec2(5, 5)))
        self.assertEqual(Vec2(5, 2), Vec2(10).min(Vec2(5, 2)))
        self.assertEqual(Vec2(5, 2), Vec2(5, 2).min(Vec2(99)))
        self.assertEqual(Vec2(5, 5), Vec2(6.5).min(Vec2(5)))
        self.assertEqual(Vec2(5.5, 5.5), Vec2(6.5).min(Vec2(5.5)))

    def test_max(self):
        self.assertEqual(Vec2(8, 5), Vec2(8, 2).max(Vec2(5, 5)))
        self.assertEqual(Vec2(10), Vec2(10).max(Vec2(5, 2)))
        self.assertEqual(Vec2(99), Vec2(5, 2).max(Vec2(99)))
        self.assertEqual(Vec2(6.5), Vec2(6.5).max(Vec2(5)))
        self.assertEqual(Vec2(6.5), Vec2(6.5).max(Vec2(5.5)))

    def test_clamp(self):
        self.assertEqual(Vec2(5, 2), Vec2(6, 2).clamp(0, 5))
        self.assertEqual(Vec2(5, 2), Vec2(0).clamp(Vec2(5, 2), 5))
        self.assertEqual(Vec2(-3, 2), Vec2(0).clamp(Vec2(-3, 2), Vec2(-3, 2)))
        self.assertEqual(Vec2(-3, 2), Vec2(0).clamp(Vec2(-30, 2), Vec2(-3, 20)))

    def test_lessThan(self):
        self.assertEqual(True, Vec2(10) < Vec2(11))
        self.assertEqual(True, Vec2(10, 10) < Vec2(11, 15))
        self.assertEqual(False, Vec2(10, 10) < Vec2(9, 15))
        self.assertEqual(False, Vec2(10, 10) < Vec2(9, 9))

    def test_greaterThan(self):
        self.assertEqual(False, Vec2(10) > Vec2(11))
        self.assertEqual(False, Vec2(10, 10) > Vec2(11, 15))
        self.assertEqual(False, Vec2(10, 10) > Vec2(9, 15))
        self.assertEqual(True, Vec2(10, 10) > Vec2(9, 9))






