from scene import Scene


class Bistro(Scene):

    def __init__(self):
        self.scenario = """
            Luna meets Aurora at the Bistro.
            'Hello,' Luna says. 'Aurora, we must leave right meow to make these deliveries on time.
            'But Luna,' says Aurora, 'it is the lunch rush and I am so hungry - allow me eat a meatball first.'
        """
        self.choices = [
            {
                "choice": "Allow Aurora to eat a meatball. Ask for one too.",
                "next_scene": "GameOver('The deliveries are late')",
                "consequences": None
            },
            {
                "choice": "Tell Aurora she can eat her meatballs on the way.",
                "next_scene": "Traffic()",
                "consequences": "aurora_hunger=False"
            },
            {
                "choice": "Tell Aurora how to do an optimal delivery and have her deliver the VIPs as compensation for Luna's valuable time",
                "next_scene": "Traffic()",
                "consequences": "aurora_hunger=True"
            }
        ]
