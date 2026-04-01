import csv
import json
import sys
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from config import get_base_url, get_default_caller_id, get_default_route, require_env
from http_client import post_json


def send_message(
    api_key: str,
    base_url: str,
    route_id: int,
    caller_id: str,
    number: str,
    message: str,
) -> dict[str, Any]:
    payload = {
        "route_id": route_id,
        "caller_id": caller_id,
        "numbers": [number],
        "message": message,
    }
    return post_json(f"{base_url}/api/v1/send_sms", api_key, payload)


def main() -> int:
    api_key = require_env("BRIDGEXAPI_API_KEY")
    base_url = get_base_url()
    route_id = get_default_route()
    caller_id = get_default_caller_id()

    csv_path = Path(__file__).with_name("numbers.csv")
    if not csv_path.exists():
        raise RuntimeError(
            f"CSV file not found: {csv_path}. Create numbers.csv in this folder."
        )

    default_message = "BridgeXAPI direct API CSV test message."
    results: list[dict[str, Any]] = []

    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)

        required_columns = {"number"}
        missing = required_columns - set(reader.fieldnames or [])
        if missing:
            raise RuntimeError(
                f"CSV is missing required column(s): {', '.join(sorted(missing))}"
            )

        for row_index, row in enumerate(reader, start=2):
            number = (row.get("number") or "").strip()
            message = (row.get("message") or default_message).strip()

            if not number:
                results.append(
                    {
                        "row": row_index,
                        "number": "",
                        "status": "SKIPPED",
                        "order_id": None,
                        "bx_message_id": None,
                        "cost": None,
                        "error": "Missing number",
                    }
                )
                continue

            try:
                data = send_message(
                    api_key=api_key,
                    base_url=base_url,
                    route_id=route_id,
                    caller_id=caller_id,
                    number=number,
                    message=message,
                )

                messages = data.get("messages") or []
                first_message = messages[0] if messages else {}
                bx_message_id = first_message.get("bx_message_id")

                results.append(
                    {
                        "row": row_index,
                        "number": number,
                        "status": "ACCEPTED",
                        "order_id": data.get("order_id"),
                        "bx_message_id": bx_message_id,
                        "cost": data.get("cost"),
                        "error": None,
                    }
                )
            except Exception as exc:
                results.append(
                    {
                        "row": row_index,
                        "number": number,
                        "status": "REJECTED",
                        "order_id": None,
                        "bx_message_id": None,
                        "cost": None,
                        "error": str(exc),
                    }
                )

    print("SUMMARY")
    print("-" * 132)
    print(
        f"{'ROW':<6}"
        f"{'NUMBER':<18}"
        f"{'STATUS':<12}"
        f"{'ORDER_ID':<12}"
        f"{'BX_MESSAGE_ID':<28}"
        f"{'COST':<10}"
        f"{'ERROR':<46}"
    )
    print("-" * 132)

    for item in results:
        order_id = str(item["order_id"]) if item["order_id"] is not None else "-"
        bx_message_id = item["bx_message_id"] or "-"
        cost = str(item["cost"]) if item["cost"] is not None else "-"
        error = item["error"] or "-"

        print(
            f"{item['row']:<6}"
            f"{item['number']:<18}"
            f"{item['status']:<12}"
            f"{order_id:<12}"
            f"{bx_message_id:<28}"
            f"{item['cost'] if item['cost'] is not None else '-':<10}"
            f"{error[:45]:<46}"
        )

    print("-" * 132)
    print("\nJSON OUTPUT\n")
    print(json.dumps(results, indent=2, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)