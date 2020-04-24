from bistro import Bistro
from game_over import GameOver
from scene import Scene
from traffic import Traffic


class DeliveryOffice(Scene):

    def __init__(self):
        self.scenario = """
            Luna is in her office at Luna's Delivery Service. The phone rings. It's Luna's sister, Aurora.
            'MEOW, Sister, MEOW!'
            'Hello, Aurora. I am here.'
            'Luna! I need your help!'
            'With what, Sister? I am working!'
            'I had a takeaway order at the Bistro. I need to make . . . a DELIVERY.'
            . . . a delivery, you say?'
        """
        self.choices = [
            {
                "choice": "Make Aurora's delivery for her - Luna needs to make a delivery of her own anyway",
                "next_scene": Traffic,
                "consequences": None
            },
            {
                "choice": "Show Aurora how to run an optimal delivery - Luna can deliver her VIPs (very important packages!!) on the way",
                "next_scene": Bistro,
                "consequences": None
            },
            {
                "choice": "Tell Aurora how to do an optimal delivery and have her deliver the VIPs as compensation for Luna's valuable time",
                "next_scene": GameOver('Aurora eats the deliveries'),
                "consequences": None
            }
        ]

