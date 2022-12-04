from enum import Enum, auto

from aoc.data import get_lines


class Shape(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


SHAPE_WINS_OVER: dict[Shape, list[Shape]] = {
    Shape.ROCK: [Shape.SCISSORS],
    Shape.PAPER: [Shape.ROCK],
    Shape.SCISSORS: [Shape.PAPER],
}


SHAPE_SCORES: dict[Shape, int] = {
    Shape.ROCK: 1,
    Shape.PAPER: 2,
    Shape.SCISSORS: 3,
}


def beats(mine: Shape, theirs: Shape) -> bool:
    return theirs in SHAPE_WINS_OVER[mine]


def solve(games: list[str]) -> int:
    opponents = {"A": Shape.ROCK, "B": Shape.PAPER, "C": Shape.SCISSORS}
    mines = {"X": Shape.ROCK, "Y": Shape.PAPER, "Z": Shape.SCISSORS}
    score = 0
    for game in games:
        opponent, mine = game.split(" ")
        opponent_shape, my_shape = opponents[opponent], mines[mine]

        score += SHAPE_SCORES[my_shape]
        if opponent_shape == my_shape:
            score += 3
        elif beats(my_shape, opponent_shape):
            score += 6

    return score


if __name__ == "__main__":
    lines = get_lines(day=2)
    solution = solve(lines)
    print(f"The final score is {solution}")
