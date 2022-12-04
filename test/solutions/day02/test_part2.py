from aoc.solutions.day02.part2 import solve


def test_input(example_input: list[str]) -> None:
    assert solve(example_input) == 12
