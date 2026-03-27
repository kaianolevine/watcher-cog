"""Watcher configuration."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class WatcherConfig:
    name: str
    folder_id: str
    deployment_id: str
    interval_min: int = 1
    idle_interval_min: int = 1
    activity_signal: str = "none"
    activity_file_id: str | None = None
    activity_threshold_min: int = 10


WATCHERS: list[WatcherConfig] = []
