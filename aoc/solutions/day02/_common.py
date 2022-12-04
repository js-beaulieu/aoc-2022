from enum import Enum, auto


class Shape(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


_SHAPE_WINS_OVER: dict[Shape, Shape] = {
    Shape.ROCK: Shape.SCISSORS,
    Shape.PAPER: Shape.ROCK,
    Shape.SCISSORS: Shape.PAPER,
}


_SHAPE_SCORES: dict[Shape, int] = {
    Shape.ROCK: 1,
    Shape.PAPER: 2,
    Shape.SCISSORS: 3,
}


def beats(mine: Shape, theirs: Shape) -> bool:
    """
    Check if a shape beats anothee
    :param mine
    :param theirs
    :return: beats it or not
    """
    return theirs == _SHAPE_WINS_OVER[mine]


def get_score_for_shape(shape: Shape) -> int:
    """
    Get the score associated to a specific shape
    :param shape: Shape to fetch the score
    :return: Score
    """
    return _SHAPE_SCORES[shape]


def get_winning_shape(shape: Shape) -> Shape:
    """
    Get the shape to win against a specific shape
    :param shape: Shape to beat
    :return: The winning shape
    """
    by_value = {v: k for k, v in _SHAPE_WINS_OVER.items()}
    return by_value[shape]


def get_losing_shape(shape: Shape) -> Shape:
    """
    Get the shape to lose against a specific shape
    :param shape: Shape to lose against
    :return: The losing shape
    """
    return _SHAPE_WINS_OVER[shape]


def get_score_for_battle(mine: Shape, theirs: Shape) -> int:
    score = get_score_for_shape(mine)
    if theirs == mine:
        score += 3
    elif beats(mine, theirs):
        score += 6
    return score
