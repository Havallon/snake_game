from game import GameObject


class Map(GameObject):
    def process(self) -> None:
        self.screen.fill('white')
