from traffic import Traffic
from bistro import Bistro
from game_over import GameOver
from deliveryoffice import DeliveryOffice
from bird_attack import BirdAttack
from win import Win


class GameMap:

    def __init__(self):
        self.delivery_office = DeliveryOffice()
        bistro = Bistro()
        game_over = GameOver

        self.scene_map = {
            self.delivery_office: [
                bistro,
                game_over
            ],
            #Bistro: [
            #    Traffic(),
            #    GameOver()
            #],
            #Traffic: [
            #    GameOver(),
            #    BirdAttack()
            #],
            #Bistro: [
            #    Win(),
            #    GameOver()
            #]
        }

    def next_scene(self, current_scene, choice):
        next_scene = self.scene_map[current_scene][choice-1]
        return next_scene

    def opening_scene(self):
        return self.delivery_office
