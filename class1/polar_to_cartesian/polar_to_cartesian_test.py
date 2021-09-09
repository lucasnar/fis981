import unittest
from polar_to_cartesian import PolarConverter

class PolarConverterTest(unittest.TestCase):
    def test_polar_to_cartesian(self):
        r = 15
        theta = 25

        cartesian_coor = PolarConverter(r, theta).convert()

        expected_x = 13.5946168055
        expected_y = 6.3392739261
        self.assertEqual(cartesian_coor, (expected_x, expected_y))

if __name__ == '__main__':
    unittest.main()
