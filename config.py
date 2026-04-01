import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent
load_dotenv(ROOT_DIR / ".env")


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def get_base_url() -> str:
    return os.getenv("BRIDGEXAPI_BASE_URL", "https://hi.bridgexapi.io").rstrip("/")


def get_timeout() -> int:
    raw = os.getenv("BRIDGEXAPI_TIMEOUT", "30")
    try:
        return int(raw)
    except ValueError as exc:
        raise RuntimeError("BRIDGEXAPI_TIMEOUT must be an integer") from exc


def get_default_route() -> int:
    raw = os.getenv("BRIDGEXAPI_ROUTE_ID", "2")
    try:
        return int(raw)
    except ValueError as exc:
        raise RuntimeError("BRIDGEXAPI_ROUTE_ID must be an integer") from exc


def get_default_caller_id() -> str:
    return os.getenv("BRIDGEXAPI_CALLER_ID", "BRIDGEXAPI")