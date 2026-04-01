# Send SMS from CSV in Python

Send messages from a CSV file using direct API.

---

## Use case

Use this when you already have data:

- Excel exports
- internal lists
- batch notifications

---

## Input file

Create:

```text
numbers.csv
```

Example:

```csv
number,message
31612345678,Verification code: 483921
31623456789,BridgeXAPI test
```

---

## Run

```bash
python send_from_csv.py
```

---

## Output

* row index
* number
* status
* order_id
* `bx_message_id`
* cost

---

## Behavior

* missing numbers are skipped
* message defaults if empty
* each row is sent separately

---

## Route selection

Uses default route from `.env`.

Inspect routes:

```bash
python ../route-pricing/routes.py
```

---

Docs: https://docs.bridgexapi.io
