from typing import TypedDict


class ScrapeSelectorResponse(TypedDict):
    url: str
    data: list[str]


class ScrapePageResponse(TypedDict, total=False):
    url: str
    title: str | None
    description: str | None
    html: str


ScrapeResponse = ScrapeSelectorResponse | ScrapePageResponse
