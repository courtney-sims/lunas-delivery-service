import unittest

from scene import Scene


class SceneTests (unittest.TestCase):

    def setUp(self):
        pass

    def test_handle_choice_success(self):
        test_scene = Scene()
        next_scene = test_scene.handle_choice(1)
        self.assertIsNone(next_scene)

    def test_handle_choice_failure(self):
        test_scene = Scene()

        with self.assertRaises(IndexError):
            test_scene.handle_choice(100)

    def tearDown(self):
        pass

