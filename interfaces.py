from dataclasses import dataclass
import requests


@dataclass
class Credentials:
    socket: str
    username: str
    password: str


@dataclass
class RestInterface:
    creds: Credentials

    @property
    def url(self) -> str:
        return f"http://{self.creds.socket}/restinterface"

    @property
    def auth(self) -> tuple[str, str]:
        return (self.creds.username, self.creds.password)

    def get(self, path: str, params: dict[str, str] = None, data: dict[str, str] = None):
        url = f"{self.url}/{path}"
        return requests.get(url, params=params, data=data, auth=self.auth)

    def post(self, path: str, params: dict[str, str] = None, data: dict[str, str] = None):
        url = f"{self.url}/{path}"
        return requests.post(url, params=params, data=data, auth=self.auth)

    def delete(self, path: str, params: dict[str, str] = None, data: dict[str, str] = None):
        url = f"{self.url}/{path}"
        return requests.delete(url, params=params, data=data, auth=self.auth)

    def put(self, path: str, params: dict[str, str] = None, data: dict[str, str] = None):
        url = f"{self.url}/{path}"
        return requests.put(url, params=params, data=data, auth=self.auth)
