from scene import Scene


class DeliveryOffice(Scene):

    def __init__(self):
        pass

    def display_scene(self):
        scenario = """
            Luna is in her office at Luna's Delivery Service. The phone rings. It's Luna's sister, Aurora.
            'MEOW, Sister, MEOW!'
            'Hello, Aurora. I am here.'
            'Luna! I need your help!'
            'With what, Sister? I am working!'
            'I had a takeaway order at the Bistro. I need to make . . . a DELIVERY.'
            . . . a delivery, you say?'
        """
        print(scenario)
        print("\nWhat should Luna do?")
