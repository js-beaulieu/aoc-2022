from itertools import groupby


def get_elves_from_lines(i: list[str]) -> list[list[int]]:
    elves_strings = [list(g) for k, g in groupby(i, key=bool) if k]
    return [[int(cal) for cal in elf] for elf in elves_strings]
