from .base import BaseAPIClient

class AccountAPIClient(BaseAPIClient):
    async def search_for_account(self, onlyActiveAccounts: bool = True):
        resp = await self._session.post("/api/Account/search", json={
            "onlyActiveAccounts": onlyActiveAccounts,
        })
        data = await self._handle_response(resp)
        return data["accounts"]