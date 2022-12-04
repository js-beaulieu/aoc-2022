from itertools import groupby

Calories = int
Elf = tuple[Calories, ...]


def get_elves_from_lines(i: list[str]) -> list[Elf]:
    elves_strings = [list(g) for k, g in groupby(i, key=bool) if k]
    return [tuple(int(cal) for cal in elf) for elf in elves_strings]
