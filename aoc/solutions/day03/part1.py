from string import ascii_letters

from aoc.data import get_lines

_PRIORITIES = list(ascii_letters)


def solve(rucksacks: list[str]) -> int:
    total_priority = 0
    for rucksack in rucksacks:
        middle = len(rucksack) // 2
        items1, items2 = set(rucksack[:middle]), set(rucksack[middle:])
        common_item = list(items1.intersection(items2))[0]
        priority = _PRIORITIES.index(common_item) + 1
        total_priority += priority
    return total_priority


if __name__ == "__main__":
    lines = get_lines(day=3)
    solution = solve(lines)
    print(f"The total of priorities is {solution}")
