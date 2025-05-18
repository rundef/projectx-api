from datetime import datetime

from .base import BaseAPIClient
from ..enums import AggregationUnit

class MarketDataAPIClient(BaseAPIClient):
    async def retrieve_bars(
        self,
        contractId: str,
        live: bool,
        startTime: datetime,
        endTime: datetime,
        unit: AggregationUnit,
        unitNumber: int,
        limit: int,
        includePartialBar: bool
    ):
        resp = await self._session.post("/api/History/retrieveBars", json={
            "contractId": contractId,
            "live": live,
            "startTime": startTime.isoformat(timespec="milliseconds") + "Z",
            "endTime": endTime.isoformat(timespec="milliseconds") + "Z",
            "unit": unit.value,
            "unitNumber": unitNumber,
            "limit": limit,
            "includePartialBar": includePartialBar,
        })
        data = await self._handle_response(resp)
        return data["bars"]

    async def search_for_contracts(self, searchText: str, live: bool):
        resp = await self._session.post("/api/Contract/search", json={
            "searchText": searchText,
            "live": live,
        })
        data = await self._handle_response(resp)
        return data["contracts"]

    async def search_for_contracts_by_id(self, contractId: str):
        resp = await self._session.post("/api/Contract/searchById", json={
            "contractId": contractId,
        })
        data = await self._handle_response(resp)
        return data["contracts"]
