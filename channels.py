from dataclasses import dataclass
from interfaces import RestInterface


@dataclass
class Channel:
    rest: RestInterface
    id: str = ""

    @property
    def url(self) -> str:
        return "channels"

    def list(self) -> list[str]:
        """List all active channels."""
        return self.rest.get(self.url)

    def get(self) -> dict[str]:
        """Get channel details."""
        url = f"{self.url}/{self.id}"
        return self.rest.get(url)
