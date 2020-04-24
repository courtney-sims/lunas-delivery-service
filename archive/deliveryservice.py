from deliveryoffice import DeliveryOffice


class DeliveryService:

    def __init__(self):
        self.aurora_hunger = True

    def play(self, current_scene):
        game_continues = True

        while game_continues:
            current_scene = current_scene()
            current_scene.display_scene()
            current_scene.display_choices()

            choice = int(input("Please provide a number"))

            current_scene = current_scene.handle_choice(choice)

            if current_scene is None:
                game_continues = False

    def feed_aurora(self):
        self.aurora_hunger = False



my_game = DeliveryService()
opening_scene = DeliveryOffice
my_game.play(opening_scene)



