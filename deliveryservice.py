from game_map import GameMap


class DeliveryService():

    def __init__(self, scene_map):
        self.scene_map = scene_map
        pass

    def play(self):
        play_scene = self.scene_map.opening_scene()
        game_continues = True

        while game_continues:
            play_scene.display_scene()
            choice = int(input("Please provide a number"))
            play_scene = self.scene_map.next_scene(play_scene,choice)


my_map = GameMap
my_game = DeliveryService(my_map)
my_game.play()



