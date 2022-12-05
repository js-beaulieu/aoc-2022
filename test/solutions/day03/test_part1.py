from aoc.solutions.day03.part1 import solve


def test_input(example_input: list[str]) -> None:
    assert solve(example_input) == 157
