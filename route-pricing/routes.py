import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from config import get_base_url, get_default_route, require_env
from http_client import get_json


def pretty(title: str, data: object) -> None:
    print(f"\n=== {title} ===")
    print(json.dumps(data, indent=2, ensure_ascii=False))


def main() -> int:
    api_key = require_env("BRIDGEXAPI_API_KEY")
    base_url = get_base_url()
    route_id = get_default_route()

    routes = get_json(f"{base_url}/api/v1/routes", api_key)
    route_detail = get_json(f"{base_url}/api/v1/routes/{route_id}", api_key)
    route_pricing = get_json(f"{base_url}/api/v1/routes/{route_id}/pricing", api_key)

    pretty("ROUTES", routes)
    pretty(f"ROUTE {route_id}", route_detail)
    pretty(f"ROUTE {route_id} PRICING", route_pricing)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)