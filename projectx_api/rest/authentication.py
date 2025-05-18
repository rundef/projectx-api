import asyncio
from datetime import datetime, timedelta

from .base import BaseAPIClient
from ..types import LoginKeyCredentials, LoginAppCredentials
from ..logger import logger

class AuthenticationAPIClient(BaseAPIClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._token: str | None = None
        self._expires_at: datetime | None = None

    async def login(self, credentials: LoginKeyCredentials | LoginAppCredentials):
        if credentials["auth_type"] == "api_key":
            url = "/api/Auth/loginKey"
            body = {
                "userName": credentials["userName"],
                "apiKey": credentials["apiKey"]
            }
        else:
            url = "/api/Auth/loginApp"
            body = {
                "userName": credentials["userName"],
                "password": credentials["password"],
                "deviceId": credentials["deviceId"],
                "appId": credentials["appId"],
                "verifyKey": credentials["verifyKey"]
            }

        resp = await self._session.post(url, json=body)
        data = await self._handle_response(resp)

        self._token = data["token"]
        self._expires_at = datetime.utcnow() + timedelta(hours=23, minutes=30)
        self._session.headers["Authorization"] = f"Bearer {self._token}"

        if len(self._bg_tasks) == 0:
            self._add_bg_task(self._revalidate_session_loop())

    async def logout(self):
        resp = await self._session.post("/api/Auth/logout")
        data = await self._handle_response(resp)

        if data.get("success"):
            await self._cancel_bg_tasks()

        return data

    async def _revalidate_session_loop(self):
        """
        Session tokens are only valid for 24 hours.
        This loop automatically re-validate the session to refresh the token
        """
        try:
            while True:
                await asyncio.sleep(600)

                if datetime.utcnow() + timedelta(minutes=10) >= self._expires_at:
                    resp = await self._session.post("/api/Auth/validate")
                    try:
                        data = await self._handle_response(resp)
                    except:
                        logger.exception("An error occurred when trying to revalidate the session")
                        continue

                    logger.info("Successfully revalidated the session")
                    self._token = data["newToken"]
                    self._expires_at = datetime.utcnow() + timedelta(hours=23, minutes=30)
                    self._session.headers["Authorization"] = f"Bearer {self._token}"
        except asyncio.CancelledError:
            pass
