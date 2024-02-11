from pygame import Surface


class GameObject:
    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        self.ready()

    def ready(self) -> None:
        pass

    def process(self) -> None:
        pass
