import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from config import get_base_url, require_env
from http_client import get_json


def main() -> int:
    api_key = require_env("BRIDGEXAPI_API_KEY")
    bx_message_id = require_env("BRIDGEXAPI_BX_MESSAGE_ID")
    base_url = get_base_url()

    data = get_json(f"{base_url}/api/v1/dlr/{bx_message_id}", api_key)
    print(json.dumps(data, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)