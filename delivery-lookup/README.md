# SMS Delivery Lookup in Python

Check message delivery using `bx_message_id`.

---

## What this does

- calls `/api/v1/dlr/<bx_message_id>`
- returns delivery status
- shows route and timestamps

---

## Setup

Set:

```env
BRIDGEXAPI_BX_MESSAGE_ID=bx_xxxxx
```

---

## Run

```bash
python get_dlr.py
```

---

## Output

* status (DELIVERED / FAILED)
* route_id
* sms_order_id
* timestamp
* error (if present)

---

Docs: https://docs.bridgexapi.io
