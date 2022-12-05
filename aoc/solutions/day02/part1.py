from aoc.data import get_lines
from aoc.solutions.day02._common import Shape, get_score_for_battle

_OPPONENTS = {"A": Shape.ROCK, "B": Shape.PAPER, "C": Shape.SCISSORS}
_MINES = {"X": Shape.ROCK, "Y": Shape.PAPER, "Z": Shape.SCISSORS}


def solve(games: list[str]) -> int:
    score = 0
    for game in games:
        opponent, mine = game.split(" ")
        opponent_shape, my_shape = _OPPONENTS[opponent], _MINES[mine]
        score += get_score_for_battle(my_shape, opponent_shape)
    return score


if __name__ == "__main__":
    lines = get_lines(day=2)
    solution = solve(lines)
    print(f"The final score is {solution}")
