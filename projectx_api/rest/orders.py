from datetime import datetime

from .base import BaseAPIClient
from ..enums import OrderType, OrderSide

class OrdersAPIClient(BaseAPIClient):
    async def search_for_orders(self, accountId: int, startTimestamp: datetime, **kwargs):
        data = {
            "accountId": accountId,
            "startTimestamp": startTimestamp.isoformat(timespec="milliseconds") + "Z"
        }
        if "endTimestamp" in kwargs:
            data["endTimestamp"] = kwargs["endTimestamp"].isoformat(timespec="milliseconds") + "Z"

        resp = await self._session.post("/api/Order/search", json=data)
        data = await self._handle_response(resp)
        return data["orders"]

    async def search_for_open_orders(self, accountId: int):
        resp = await self._session.post("/api/Order/searchOpen", json={
            "accountId": accountId,
        })
        data = await self._handle_response(resp)
        return data["orders"]

    async def place_order(
        self,
        accountId: int,
        contractId: str,
        type: OrderType,
        side: OrderSide,
        size: int,
        **kwargs
    ):
        data = {
            "accountId": accountId,
            "contractId": contractId,
            "type": type.value,
            "side": side.value,
            "size": size,
        }
        data.update(kwargs)

        resp = await self._session.post("/api/Order/place", json=data)
        data = await self._handle_response(resp)
        return data

    async def cancel_order(self, accountId: int, orderId: int):
        resp = await self._session.post("/api/Order/cancel", json={
            "accountId": accountId,
            "orderId": orderId,
        })
        data = await self._handle_response(resp)
        return data

    async def modify_order(self, accountId: int, orderId: int, **kwargs):
        data = {
            "accountId": accountId,
            "orderId": orderId,
        }
        data.update(kwargs)

        resp = await self._session.post("/api/Order/modify", json=data)
        data = await self._handle_response(resp)
        return data