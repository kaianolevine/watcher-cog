"""Pytest configuration."""

import pytest


class DummyDriveFile:
    def __init__(self, file_id: str, name: str = "file.txt") -> None:
        self.id = file_id
        self.name = name
        self.mime_type = None
        self.modified_time = None


@pytest.fixture
def dummy_drive_file() -> type[DummyDriveFile]:
    return DummyDriveFile

