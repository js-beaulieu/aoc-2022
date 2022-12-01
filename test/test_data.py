from pathlib import Path

import pytest
from pytest_mock import MockFixture

from aoc.data import DataError, get_input, get_lines


@pytest.fixture(autouse=True)
def mock_data_file(mocker: MockFixture, tmp_path: Path) -> Path:
    mocker.patch("aoc.data.DATA_PATH", new=tmp_path)
    tmp_file = (tmp_path / "01").with_suffix(".txt")
    tmp_file.touch()
    tmp_file.write_text("foo\n\nbar\n")
    return tmp_file


class TestGetInput:
    def test_returns_the_file_contents_when_exists(self) -> None:
        result = get_input(day=1)
        assert result == "foo\n\nbar\n"

    def test_throws_when_file_doesnt_exist(self) -> None:
        with pytest.raises(DataError):
            get_input(day=42)


class TestGetLines:
    def test_returns_file_contents_as_array(self) -> None:
        assert get_lines(day=1) == ["foo", "", "bar"]
