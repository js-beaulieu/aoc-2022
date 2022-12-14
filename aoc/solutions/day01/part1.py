from aoc.data import get_lines
from aoc.solutions.day01._common import get_elves_from_lines


def solve(lines: list[str]) -> int:
    calories_groups = get_elves_from_lines(lines)
    return max(sum(group) for group in calories_groups)


if __name__ == "__main__":
    lines = get_lines(day=1)
    solution = solve(lines)
    print(f"The largest amount of calories is {solution}")
