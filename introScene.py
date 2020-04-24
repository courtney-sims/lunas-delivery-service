class IntroScene:
    def run(self):
        self.print_scene()
        self.print_options()
        choice = self.get_user_input()
        next_scene = self.get_next_scene(choice)
        return next_scene

    def get_next_scene(self, choice):
        if choice == 1:
            return "Traffic"
        elif choice == 2:
            return "Bistro"
        elif choice == 3:
            return "GameOver"
        else:
            return "Invalid selection"

    def get_user_input(self):
        return input("\nWhat should Luna do?")

    def print_options(self):
        print("""
        1. Make Aurora's delivery for her - Luna needs to make a delivery of her own anyway
        2. Show Aurora how to run an optimal delivery - Luna can deliver her VIPs (very important packages!!) on the way
        3. Tell Aurora how to do an optimal delivery and have her deliver the VIPs as compensation for Luna's valuable time
        """)

    def print_scene(self):
        print("""
            Luna is in her office at Luna's Delivery Service. The phone rings. It's Luna's sister, Aurora.
            'MEOW, Sister, MEOW!'
            'Hello, Aurora. I am here.'
            'Luna! I need your help!'
            'With what, Sister? I am working!'
            'I had a takeaway order at the Bistro. I need to make . . . a DELIVERY.'
            . . . a delivery, you say?'
        """)
