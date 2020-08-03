import requests
import os
from requests.models import Response
import uvicorn
import urllib.parse

from fastapi import FastAPI

app = FastAPI()


def _get_auth_token() -> str:
    return os.getenv("API_TOKEN")


def _http_get(url: str) -> Response:
    url = f"https://api.clashofclans.com/v1/{url}"
    print(f"fetching {url}")
    headers = {"Authorization": f"Bearer {_get_auth_token()}"}

    return requests.get(url, headers=headers)


def _get_clan_info(clan_tag: str):
    tag = urllib.parse.quote(clan_tag)
    url = f"clans/{tag}"
    r = _http_get(url)

    return r.json()


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/clans/{clan_tag}")
def get_clan_info(clan_tag: str):
    print(clan_tag)
    return _get_clan_info(clan_tag)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
