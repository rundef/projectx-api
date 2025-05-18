from datetime import datetime

from .base import BaseAPIClient

class TradesAPIClient(BaseAPIClient):
    async def search_for_trades(self, accountId: int, startTimestamp: datetime, **kwargs):
        data = {
            "accountId": accountId,
            "startTimestamp": startTimestamp.isoformat(timespec="milliseconds") + "Z"
        }
        if "endTimestamp" in kwargs:
            data["endTimestamp"] = kwargs["endTimestamp"].isoformat(timespec="milliseconds") + "Z"

        resp = await self._session.post("/api/Trade/search", json=data)
        data = await self._handle_response(resp)
        return data["trades"]
