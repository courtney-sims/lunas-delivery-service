from game_map import GameMap


class DeliveryService:

    def __init__(self, scene_mapping):
        self.scene_mapping = scene_mapping

    def play(self):
        play_scene = self.scene_mapping.opening_scene()
        game_continues = True

        while game_continues:
            play_scene.display_scene()
            choice = int(input("Please provide a number"))
            play_scene = self.scene_mapping.next_scene(play_scene, choice)


my_map = GameMap()
my_game = DeliveryService(my_map)
my_game.play()



