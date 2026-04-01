import json
from typing import Any

import requests

from config import get_timeout


def build_headers(api_key: str, json_request: bool = False) -> dict[str, str]:
    headers = {
        "X-API-KEY": api_key,
        "Accept": "application/json",
    }
    if json_request:
        headers["Content-Type"] = "application/json"
    return headers


def parse_json_response(response: requests.Response) -> Any:
    try:
        return response.json()
    except ValueError as exc:
        raise RuntimeError(f"Non-JSON response received: {response.text}") from exc


def get_json(url: str, api_key: str) -> Any:
    try:
        response = requests.get(
            url,
            headers=build_headers(api_key),
            timeout=get_timeout(),
        )
    except requests.RequestException as exc:
        raise RuntimeError(f"Network error during GET {url}: {exc}") from exc

    data = parse_json_response(response)

    if not response.ok:
        raise RuntimeError(
            f"GET {url} failed (status={response.status_code}) (body={json.dumps(data)})"
        )

    return data


def post_json(url: str, api_key: str, payload: dict[str, Any]) -> Any:
    try:
        response = requests.post(
            url,
            headers=build_headers(api_key, json_request=True),
            json=payload,
            timeout=get_timeout(),
        )
    except requests.RequestException as exc:
        raise RuntimeError(f"Network error during POST {url}: {exc}") from exc

    data = parse_json_response(response)

    if not response.ok:
        raise RuntimeError(
            f"POST {url} failed (status={response.status_code}) (body={json.dumps(data)})"
        )

    return data