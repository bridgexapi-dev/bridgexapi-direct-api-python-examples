import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from config import (
    get_base_url,
    get_default_caller_id,
    get_default_route,
    require_env,
)
from http_client import post_json


def main() -> int:
    api_key = require_env("BRIDGEXAPI_API_KEY")
    test_number = require_env("BRIDGEXAPI_TEST_NUMBER")
    base_url = get_base_url()
    route_id = get_default_route()
    caller_id = get_default_caller_id()

    payload = {
        "route_id": route_id,
        "caller_id": caller_id,
        "numbers": [test_number],
        "message": "Verification code: 483921",
    }

    data = post_json(f"{base_url}/api/v1/estimate", api_key, payload)
    print(json.dumps(data, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)