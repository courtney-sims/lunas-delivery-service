import abc


class Scene:

    def __init__(self):
        self.scenario = """
            More coming soon!
        """
        self.choices = [
            {
                "choice": "Press the number 1 to exit",
                "next_scene": None,
                "consequences": None
            }
        ]

    def display_scene(self):
        print(self.scenario)
        print("\nWhat should Luna do?")

    def display_choices(self):
        opt_num = 1
        for option in self.choices:
            print(f'{opt_num}. {option["choice"]}')
            opt_num += 1

    def handle_choice(self, choice):
        next_scene = self.choices[choice - 1]["next_scene"]
        return next_scene

