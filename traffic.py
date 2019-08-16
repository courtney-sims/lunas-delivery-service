from scene import Scene


class Traffic(Scene):
    def __init__(self):
        self.scenario = """
            Luna begins the delivery route with great speed and efficiency.
            Halfway through the route, she encounters a traffic jam.
        """
        self.choices = [
            {
                "choice": "Wait patiently for the traffic to clear up. Luna knows to plan for the unexpected in her timetables.",
                "next_scene": None,
                "consequences": None,
            },
            {
                "choice": "Hitch a ride with someone.",
                "next_scene": None,
                "consequences": None,
            }
        ]

    def handle_choice(self, choice):
        choice = self.choices[choice-1]
        consequences = choice["consequences"]()

        next_scene = choice["next_scene"]

        return next_scene


if delivery