import pytest


@pytest.fixture
def example_input() -> list[str]:
    return """A Y
B X
C Z
""".splitlines()
