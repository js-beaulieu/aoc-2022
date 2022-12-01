import pytest


@pytest.fixture
def example_input() -> list[str]:
    return """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".splitlines()
