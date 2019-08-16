from scene import Scene


class GameOver(Scene):
    def __init__(self, reason):
        super(GameOver, self).__init__()
        self.reason = reason
        self.scenario = """
            GAME OVER:
        """

    def display_scene(self):
        print(self.scenario)
        print(self.reason)

