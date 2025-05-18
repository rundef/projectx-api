from .base import BaseAPIClient

class PositionsAPIClient(BaseAPIClient):
    async def search_for_positions(self, accountId: int):
        resp = await self._session.post("/api/Position/searchOpen", json={
            "accountId": accountId
        })
        data = await self._handle_response(resp)
        return data["positions"]

    async def close_position(self, accountId: int, contractId: str):
        resp = await self._session.post("/api/Position/closeContract", json={
            "accountId": accountId,
            "contractId": contractId
        })
        data = await self._handle_response(resp)
        return data

    async def partially_close_position(self, accountId: int, contractId: str, size: int):
        resp = await self._session.post("/api/Position/partialCloseContract", json={
            "accountId": accountId,
            "contractId": contractId,
            "size": size
        })
        data = await self._handle_response(resp)
        return data