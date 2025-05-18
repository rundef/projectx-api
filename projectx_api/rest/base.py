import httpx
import asyncio

from ..exceptions import ProjectXAPIError, StatusCodeError

class BaseAPIClient:
    def __init__(self, session: httpx.AsyncClient):
        self._session = session
        self._bg_tasks = []

    def _add_bg_task(self, coro):
        task = asyncio.create_task(coro)
        self._bg_tasks.append(task)

    async def _cancel_bg_tasks(self):
        for task in self._bg_tasks:
            task.cancel()

        for task in self._bg_tasks:
            try:
                await task
            except asyncio.CancelledError:
                pass

        self._bg_tasks.clear()

    async def _handle_response(self, response: httpx.Response) -> dict:
        if response.status_code != 200:
            raise StatusCodeError(f"HTTP error: {response.status_code} - {response.text}")

        data = await response.json()

        if not data.get("success") or data.get("errorCode", 0) != 0:
            raise ProjectXAPIError(
                code=data.get("errorCode", -1),
                message=data.get("errorMessage", "Unknown error")
            )

        return data