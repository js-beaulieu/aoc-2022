from aoc.data import get_lines
from aoc.solutions.day02._common import (
    Shape,
    get_losing_shape,
    get_score_for_battle,
    get_winning_shape,
)


def solve(games: list[str]) -> int:
    opponents = {"A": Shape.ROCK, "B": Shape.PAPER, "C": Shape.SCISSORS}

    score = 0
    for game in games:
        opponent, action = game.split(" ")
        opponent_shape = opponents[opponent]
        match action:
            case "X":
                my_shape = get_losing_shape(opponent_shape)
            case "Y":
                my_shape = opponent_shape
            case "Z":
                my_shape = get_winning_shape(opponent_shape)
            case _:
                # should never happen, in theory
                raise RuntimeError("Could not figure out a right move")

        score += get_score_for_battle(my_shape, opponent_shape)

    return score


if __name__ == "__main__":
    lines = get_lines(day=2)
    solution = solve(lines)
    print(f"The final score is {solution}")
