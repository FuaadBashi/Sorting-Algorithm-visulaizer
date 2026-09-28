"""Pygame front end: watch sorting algorithms rearrange a list of bars."""

import random

import pygame

from algorithms import ALGORITHMS

WIDTH, HEIGHT = 1000, 700
SIDE_PADDING = 80
TOP_PADDING = 120
FPS = 60

BACKGROUND = (24, 26, 33)
TEXT = (230, 232, 238)
MUTED = (150, 155, 170)
BAR_SHADES = [(110, 118, 140), (130, 138, 160), (150, 158, 180)]
ROLE_COLOURS = {
    "compare": (240, 200, 80),
    "swap": (235, 90, 90),
    "pivot": (90, 150, 240),
    "placed": (90, 200, 120),
}


def new_list(n: int = 50, low: int = 1, high: int = 100) -> list[int]:
    return [random.randint(low, high) for _ in range(n)]


def draw(screen, fonts, values, highlights, title, subtitle) -> None:
    screen.fill(BACKGROUND)
    heading = fonts["large"].render(title, True, TEXT)
    screen.blit(heading, (WIDTH / 2 - heading.get_width() / 2, 20))
    for row, text in enumerate(subtitle):
        line = fonts["small"].render(text, True, MUTED)
        screen.blit(line, (WIDTH / 2 - line.get_width() / 2, 60 + row * 22))

    low, high = min(values), max(values)
    span = max(high - low, 1)  # a list of equal values used to divide by zero
    bar_width = (WIDTH - SIDE_PADDING) / len(values)
    usable = HEIGHT - TOP_PADDING - 20
    for i, value in enumerate(values):
        # Scale by height, not width, and keep a minimum so the smallest value stays visible.
        bar_height = 10 + (value - low) / span * (usable - 10)
        x = SIDE_PADDING / 2 + i * bar_width
        colour = ROLE_COLOURS.get(highlights.get(i), BAR_SHADES[i % 3])
        pygame.draw.rect(
            screen, colour, (x, HEIGHT - bar_height, max(bar_width - 1, 1), bar_height)
        )
    pygame.display.flip()


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sorting Algorithm Visualizer")
    fonts = {
        "large": pygame.font.SysFont("arial", 28, bold=True),
        "small": pygame.font.SysFont("arial", 18),
    }
    clock = pygame.time.Clock()

    values = new_list()
    key, ascending = "b", True
    steps, highlights = None, {}
    subtitle = [
        "SPACE start  ·  R new list  ·  A ascending  ·  D descending",
        "B bubble  ·  I insertion  ·  S selection  ·  M merge  ·  Q quick",
    ]

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and steps is None:
                name = pygame.key.name(event.key)
                if name == "space":
                    steps = ALGORITHMS[key][1](values, ascending)
                elif name == "r":
                    values, highlights = new_list(), {}
                elif name in ("a", "d"):
                    ascending = name == "a"
                elif name in ALGORITHMS:
                    key = name
            elif event.type == pygame.KEYDOWN and pygame.key.name(event.key) == "r":
                values, steps, highlights = new_list(), None, {}

        if steps is not None:
            highlights = next(steps, None)
            if highlights is None:
                steps, highlights = None, {}

        order = "Ascending" if ascending else "Descending"
        draw(screen, fonts, values, highlights or {}, f"{ALGORITHMS[key][0]} · {order}", subtitle)

    pygame.quit()


if __name__ == "__main__":
    main()
