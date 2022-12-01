from pathlib import Path

DATA_PATH: Path = Path(__file__).parent.parent / "data" / "days"


class DataError(Exception):
    pass


def get_input(*, day: int) -> str:
    """
    Get raw string input for a given day
    :param day: Number of the day of the month
    :return: Raw data file contents as a string
    """
    day_path = (DATA_PATH / f"{day:02d}").with_suffix(".txt")
    if not day_path.exists() or not day_path.is_file():
        raise DataError(f"No data available for day {day}")
    return day_path.read_text("utf-8")
