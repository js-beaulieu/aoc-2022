from aoc.solutions.day01.part2 import solve


def test_input(example_input: list[str]) -> None:
    assert solve(example_input) == 45000
