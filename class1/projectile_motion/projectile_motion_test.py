import unittest
from projectile_motion import ProjectileMotion

class ProjectileMotionTest(unittest.TestCase):
    def test_projectile_motion_params(self):
        v = 30
        theta = 30

        projectile_motion_params = ProjectileMotion(v, theta).params()

        expected_params = {"max_height": 11.25, "horizontal_reach": 77.94}

        self.assertEqual(projectile_motion_params, expected_params)

if __name__ == '__main__':
    unittest.main()
