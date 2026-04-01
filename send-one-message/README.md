# Send SMS in Python (Direct API)

Send a single SMS using a direct HTTP request.

No SDK required.

---

## What this does

- submits a message via `/api/v1/send_sms`
- returns `order_id`
- returns `bx_message_id`
- shows cost and status

---

## Run

```bash
python send_one.py
```

---

## Route selection

This script uses a default `route_id` from your `.env`.

To inspect available routes:

```bash
python ../route-pricing/routes.py
```

---

## Output

* order ID
* `bx_message_id`
* cost

---

Docs: https://docs.bridgexapi.io
