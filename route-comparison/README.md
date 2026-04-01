# Compare SMS Routes in Python

Send the same message across multiple routes.

---

## What this does

- sends messages across multiple route IDs
- prints acceptance status
- returns cost per route
- shows `bx_message_id`
- allows handset comparison

---

## Run

```bash
python compare_routes.py
```

---

## Output

* route_id
* status
* order_id
* `bx_message_id`
* cost

---

## Important

Routes in this example are sample values.

Check available routes first:

```bash
python ../route-pricing/routes.py
```

---

## Purpose

This is not a benchmark.

This is a practical comparison of routing behavior.

---

Docs: https://docs.bridgexapi.io
