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

    def __post_init__(self) -> None:
        if self.idle_interval_min == 1 and self.interval_min != 1:
            object.__setattr__(self, "idle_interval_min", self.interval_min)


WATCHERS: list[WatcherConfig] = []
