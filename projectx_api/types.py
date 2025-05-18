from typing import Literal, TypedDict

class LoginKeyCredentials(TypedDict):
    auth_type: Literal["api_key"]
    userName: str
    apiKey: str

class LoginAppCredentials(TypedDict):
    auth_type: Literal["app"]
    userName: str
    password: str
    deviceId: str
    appId: str
    verifyKey: str
