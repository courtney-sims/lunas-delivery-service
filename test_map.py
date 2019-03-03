import unittest

from game_map import GameMap
from scene import Scene
from deliveryoffice import DeliveryOffice
from traffic import Traffic


class MapTests (unittest.TestCase):

    def setUp(self):
        pass

    def test_next_scene_success(self):
        test_map = GameMap()
        test_deliveryoffice = DeliveryOffice
        next_scene = test_map.next_scene(test_deliveryoffice, 1)
        self.assertEqual(next_scene, Traffic)

    def test_next_scene_failure(self):
        test_map = GameMap()

        with self.assertRaises(IndexError):
            test_deliveryoffice = DeliveryOffice
            test_map.next_scene(test_deliveryoffice, 5)

        with self.assertRaises(KeyError):
            test_map.next_scene(test_map, 1)

    def test_opening_scene(self):
        my_map = GameMap()
        opening_scene = my_map.opening_scene()
        self.assertTrue(issubclass(opening_scene, Scene))

    def tearDown(self):
        pass

