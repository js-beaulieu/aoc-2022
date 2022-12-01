from aoc.data import get_lines
from aoc.solutions.day01._common import get_elves_from_lines


def solve(lines: list[str]) -> int:
    calories_groups = get_elves_from_lines(lines)
    data = sorted((sum(group) for group in calories_groups), reverse=True)
    return sum(data[0:3])


if __name__ == "__main__":
    lines = get_lines(day=1)
    solution = solve(lines)
    print(f"The largest amount of calories is {solution}")
