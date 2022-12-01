from pathlib import Path

import pytest
from pytest_mock import MockFixture

from aoc.data import DataError, get_input


class TestGetInput:
    @pytest.fixture(autouse=True)
    def mock_data_path(self, mocker: MockFixture, tmp_path: Path) -> Path:
        mocker.patch("aoc.data.DATA_PATH", new=tmp_path)
        return tmp_path

    def test_returns_the_file_contents_when_exists(self, mock_data_path: Path) -> None:
        tmp_file = (mock_data_path / "01").with_suffix(".txt")
        tmp_file.touch()
        tmp_file.write_text("foo\nbar\n")

        result = get_input(day=1)
        assert result == "foo\nbar\n"

    def test_throws_when_file_doesnt_exist(self) -> None:
        with pytest.raises(DataError):
            get_input(day=42)
