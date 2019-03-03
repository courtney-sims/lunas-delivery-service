import unittest

from game_map import GameMap
from scene import Scene
from deliveryoffice import DeliveryOffice
from bistro import Bistro


class MapTests (unittest.TestCase):

    def setUp(self):
        pass

    def test_next_scene_success(self):
        test_map = GameMap()
        opening_scene = test_map.opening_scene()
        next_scene = test_map.next_scene(opening_scene, 1)
        self.assertIsInstance(next_scene, Scene)

    def test_next_scene_failure(self):
        test_map = GameMap()

        with self.assertRaises(IndexError):
            opening_scene = test_map.opening_scene()
            test_map.next_scene(opening_scene, 100)

        with self.assertRaises(KeyError):
            test_map.next_scene(test_map, 1)

    def test_opening_scene(self):
        my_map = GameMap()
        opening_scene = my_map.opening_scene()
        self.assertIsInstance(opening_scene, Scene)

    def tearDown(self):
        pass

