

class Scene:

    def __init__(self, scene_name):
        self.scene_name = scene_name

    def display_scene(self):
        # get scenario from json for self.scene_name
        scenario = """
            Test scenario
        """
        print(scenario)
        print("\nWhat should Luna do?")

    def make_choice(self, choice):
        # get choices from json for self.scene_name
        choices = [
            {
                "Choice": "Test choice",
                "Consequences": "Test consequence",
                "NextScene": "NextTestScene"
            },
        ]
        #change_state(self.choices[choice]["Consequences"])
        return choices[choice-1]["NextScene"]
