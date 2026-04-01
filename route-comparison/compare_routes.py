import sys
import time
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from config import get_base_url, get_default_caller_id, require_env
from http_client import post_json


def main() -> int:
    api_key = require_env("BRIDGEXAPI_API_KEY")
    target_number = require_env("BRIDGEXAPI_TEST_NUMBER")
    base_url = get_base_url()
    caller_id = get_default_caller_id()

    # Example routes for comparison. Inspect available routes first in route-pricing/routes.py
    routes_to_test = [1, 2, 3, 4]
    results: list[dict[str, Any]] = []

    print("\nBridgeXAPI direct API route comparison")
    print(f"Recipient: {target_number}\n")

    for route_id in routes_to_test:
        handset_ref = f"R{route_id}"
        payload = {
            "route_id": route_id,
            "caller_id": caller_id,
            "numbers": [target_number],
            "message": f"BridgeXAPI verification notice. Ref: {handset_ref}.",
        }

        try:
            data = post_json(f"{base_url}/api/v1/send_sms", api_key, payload)

            messages = data.get("messages") or []
            first_message = messages[0] if messages else {}
            bx_message_id = first_message.get("bx_message_id")

            print(f"[Route {route_id}] ACCEPTED")
            print(f"  order_id      : {data.get('order_id')}")
            print(f"  bx_message_id : {bx_message_id}")
            print(f"  cost          : {data.get('cost')}")
            print(f"  handset_ref   : {handset_ref}")
            print()

            results.append(
                {
                    "route_id": route_id,
                    "status": "ACCEPTED",
                    "order_id": data.get("order_id"),
                    "bx_message_id": bx_message_id,
                    "cost": data.get("cost"),
                    "handset_ref": handset_ref,
                    "error": None,
                }
            )
        except Exception as exc:
            print(f"[Route {route_id}] REJECTED")
            print(f"  reason        : {exc}")
            print()

            results.append(
                {
                    "route_id": route_id,
                    "status": "REJECTED",
                    "order_id": None,
                    "bx_message_id": None,
                    "cost": None,
                    "handset_ref": handset_ref,
                    "error": str(exc),
                }
            )

        time.sleep(1.0)

    print("SUMMARY")
    print("-" * 110)
    print(
        f"{'ROUTE':<8}"
        f"{'STATUS':<12}"
        f"{'ORDER_ID':<12}"
        f"{'BX_MESSAGE_ID':<28}"
        f"{'HANDSET_REF':<14}"
        f"{'COST':<10}"
    )
    print("-" * 110)

    for item in results:
        order_id = str(item["order_id"]) if item["order_id"] is not None else "-"
        bx_message_id = item["bx_message_id"] or "-"
        cost = str(item["cost"]) if item["cost"] is not None else "-"

        print(
            f"{item['route_id']:<8}"
            f"{item['status']:<12}"
            f"{order_id:<12}"
            f"{bx_message_id:<28}"
            f"{item['handset_ref']:<14}"
            f"{cost:<10}"
        )

    print("-" * 110)
    print("\nCheck your handset to compare what lands per route.\n")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)