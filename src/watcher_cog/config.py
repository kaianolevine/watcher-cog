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


WATCHERS: list[WatcherConfig] = [
    WatcherConfig(
        name="dj-sets",
        folder_id="1t4d_8lMC3ZJfSyainbpwInoDta7n69hC",
        deployment_id="d898461d-0d9f-40b0-aa2e-9a75bc266f94",
        interval_min=1,
    ),
    WatcherConfig(
        name="live-history",
        folder_id="1HGxEr5ocY9JLtXcJqDRIOD95rXU6QLUW",
        deployment_id="4bb81b41-0c9b-4c13-a0af-60d8646b2e2d",
        interval_min=1,
    ),
    # generate-summaries and update-dj-set-collection are triggered
    # manually or via Prefect schedules, not by Drive file drops
    # Add them here if you want Drive-triggered runs for those too
    # Deployment 'update-dj-set-collection/update-dj-set-collection'
    # id '88e08291-3ca4-417c-92e0-649cb93e2cc8'.
    # Deployment 'generate-summaries/generate-summaries'
    # id 'ad3808da-dc8a-4e4c-b633-ee71534a0c1e'.
]
