import requests
import json
import os
from urllib import parse
from typing import List


def _get_auth_token() -> str:
    return os.getenv("API_TOKEN")


def _get_clan_tag() -> str:
    return parse.quote(os.getenv("CLAN_TAG"))


url = "https://api.clashofclans.com/v1/clans/{}/currentwar".format(_get_clan_tag())
headers = {"Authorization": "Bearer {}".format(_get_auth_token())}

r = requests.get(url, headers=headers)

current_war = json.loads(r.text)
members: List[dict] = current_war.get("clan").get("members")
members.sort(key=lambda x: x.get("mapPosition"))

for member in members:
    print("#{}: {}".format(member.get("mapPosition"), member.get("name")))
    print("Attacks: {}".format(len(member.get("attacks", []),)))
