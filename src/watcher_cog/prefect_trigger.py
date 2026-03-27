"""Prefect trigger client."""

from __future__ import annotations

import os

import httpx

from watcher_cog.logger import log


async def fire(deployment_id: str) -> None:
    """Trigger a Prefect deployment run."""
    api_key = os.getenv("PREFECT_API_KEY", "").strip()
    api_url = os.getenv("PREFECT_API_URL", "").strip().rstrip("/")

    if not api_key:
        raise RuntimeError("PREFECT_API_KEY is not set")
    if not api_url:
        raise RuntimeError("PREFECT_API_URL is not set")

    endpoint = f"{api_url}/deployments/{deployment_id}/create_flow_run"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(endpoint, headers=headers, json={})
        log.info(
            "prefect trigger fired deployment_id=%s status=%s",
            deployment_id,
            response.status_code,
        )
        response.raise_for_status()
