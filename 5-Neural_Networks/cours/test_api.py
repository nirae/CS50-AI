#! /usr/bin/env python3

import httpx
import json
from tqdm import tqdm


CLIENT_ID = "89f9bc394bb089754bed4bfe02253c76503362506d2ab8c261c632dc705ceed1"
CLIENT_SECRET = "828bb889a9eb5392be7c4766535b54174c16e815feb7b85faf7b3069c8b77c8a"
TOKEN_URL = "https://api.intra.42.fr/oauth/token"
REDIRECT_URI = "http://0.0.0.0:5000/callback"
TOKEN = "507b8b9a7d255ea2983a8302117f5a34bb2ca3d276c80f476ff391db79b1f012"

def get_token():
    # curl -X POST --data "grant_type=client_credentials&client_id=MY_AWESOME_UID&client_secret=MY_AWESOME_SECRET" https://api.intra.42.fr/oauth/token
    post_data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    r = httpx.post(
        TOKEN_URL,
        data=post_data
    )
    token_json = r.json()
    return token_json["access_token"]



if __name__ == "__main__":

    token = get_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    seen_users = []

    for i in range(100):
        print(f"PAGE {i}", f"https://api.intra.42.fr/v2/campus/1/locations?page[size]=100&page[number]={i}")
        r = httpx.get(f"https://api.intra.42.fr/v2/campus/1/locations?page[size]=100&page[number]={i}", headers=headers)
        while r.status_code == 429:
            r = httpx.get(f"https://api.intra.42.fr/v2/campus/1/locations?page[size]=100&page[number]={i}", headers=headers)

        result = r.json()
        for user in tqdm(result):
            if user['user']['id'] in seen_users:
                continue
            res = httpx.get(f"https://api.intra.42.fr/v2/users/{user['user']['id']}", headers=headers)
            while res.status_code == 429:
                res = httpx.get(f"https://api.intra.42.fr/v2/users/{user['user']['id']}", headers=headers)
            data = res.json()
            for cursus in data['cursus_users']:
                if cursus['cursus']['name'] == "42cursus":
                    if cursus['level'] > 19:
                        print(user['host'], data['login'], cursus['level'])
            seen_users.append(user['user']['id'])