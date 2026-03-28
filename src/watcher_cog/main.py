"""Application entrypoint."""

from __future__ import annotations

import asyncio
import os
import sys

import sentry_sdk
from dotenv import load_dotenv

from watcher_cog.config import WATCHERS
from watcher_cog.logger import log
from watcher_cog.watcher import run_watcher


async def main() -> None:
    """Run all configured watcher tasks."""
    load_dotenv()
    sentry_sdk.init(dsn=os.getenv("SENTRY_DSN"), environment="production")

    if not WATCHERS:
        log.warning("no watchers configured - exiting")
        return

    watcher_names = ", ".join(watcher.name for watcher in WATCHERS)
    log.info("starting %s watcher(s): %s", len(WATCHERS), watcher_names)

    tasks = [run_watcher(watcher) for watcher in WATCHERS]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)
