import random
import sys
from collections import deque, namedtuple

import pygame

width = 800
height = 600

Column = namedtuple("Column", ["tiles", "height"])


class Map:
    def __init__(self) -> None:
        self.rows = 20
        self.columns = 20
        self.delta = 1
        self.last_height = 15
        self.player = self.columns // 2
        ####
        self.tiles = deque(
            [self.random_column() for _ in range(self.columns)], maxlen=self.columns
        )
        ####

    def random_column(self):
        column_height = random.randint(
            self.last_height - self.delta, self.last_height + self.delta
        )
        column_height = min(self.columns - 1, max(0, column_height))
        self.last_height = column_height

        tiles = [0] * column_height
        tiles.extend([1] * (self.columns - column_height))

        assert len(tiles) == self.columns
        return Column(tiles, column_height)

    def forward(self):
        ####
        self.tiles.append(self.random_column())
        ####

    def render(self):
        for x in range(self.rows):
            for y in range(self.columns):
                pygame.draw.rect(
                    screen,
                    "black" if self.tiles[x].tiles[y] else "white",
                    (
                        x * width // self.rows,
                        y * height // self.columns,
                        width // self.rows,
                        height // self.columns + 1,
                    ),
                )

        pygame.draw.rect(
            screen,
            "red",
            (
                (
                    self.player * width // self.rows,
                    (self.tiles[self.player].height - 1) * height // self.columns,
                ),
                (
                    width // self.rows,
                    height // self.columns,
                ),
            ),
        )


map_ = Map()

screen = pygame.display.set_mode((width, height))
screen.fill("white")
while True:
    for event in pygame.event.get():
        if event.type in [pygame.QUIT]:
            sys.exit()
    map_.forward()
    map_.render()
    pygame.display.update()
    pygame.time.delay(250)