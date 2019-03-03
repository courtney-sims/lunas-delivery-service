from deliveryoffice import DeliveryOffice
from traffic import Traffic
from bistro import Bistro
from game_over import GameOver


class GameMap:

    def __init__(self):

        self.scene_map = {
            DeliveryOffice: [
                Traffic,
                Bistro,
                GameOver,
            ]
        }

    def next_scene(self, current_scene, choice):
        next_scene = self.scene_map[current_scene][choice-1]
        return next_scene

    def opening_scene(self):
        delivery_office = DeliveryOffice
        return delivery_office
