from typing import Any

from octopus.ext_api.base import CIAdapter


class JenkinsAdapter(CIAdapter):
    """Jenkins CI platform adapter implementation."""

    def __init__(self, api_url: str, token: str):
        super().__init__(api_url, token)

    def get_pipeline_status(self, pipeline_id: str) -> dict[str, Any]:
        """Get Jenkins pipeline status."""
        pass
