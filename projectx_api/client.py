from pattern_kit import DelegateMixin
import httpx
import atexit
import asyncio

from .enums import ConnectionURLS
from .rest import (
    AuthenticationAPIClient,
    AccountAPIClient,
    MarketDataAPIClient,
    OrdersAPIClient,
    PositionsAPIClient,
    TradesAPIClient,
)

class ProjectXClient(DelegateMixin):
    def __init__(self, env: ConnectionURLS):
        self.env = env
        self.session = httpx.AsyncClient(base_url=env.api_endpoint)

        self.rest_clients = {
            "authentication": AuthenticationAPIClient(self.session),
            "account": AccountAPIClient(self.session),
            "market_data": MarketDataAPIClient(self.session),
            "orders": OrdersAPIClient(self.session),
            "positions": PositionsAPIClient(self.session),
            "trades": TradesAPIClient(self.session),
        }

        for client in self.rest_clients.values():
            self._delegate_methods(client)

        atexit.register(self._shutdown_hook)

    def _shutdown_hook(self):
        try:
            loop = asyncio.get_event_loop()
            if loop.is_closed():
                return
            loop.run_until_complete(self._cancel_all_bg_tasks())
        except Exception:
            pass

    async def _cancel_all_bg_tasks(self):
        for client in self.rest_clients.values():
            await client._cancel_bg_tasks()

    async def ping(self):
        return await self.session.post("/api/Status/ping")
