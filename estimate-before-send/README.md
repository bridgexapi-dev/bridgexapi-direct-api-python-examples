# Estimate SMS Cost in Python (Direct API)

Calculate SMS cost before sending.

---

## What this does

- calls `/api/v1/estimate`
- returns estimated cost
- returns account balance
- shows if balance is sufficient

---

## Run

```bash
python estimate.py
```

---

## Why this matters

SMS pricing is not fixed.

Cost depends on:

* route
* destination prefix
* inventory

---

## Route selection

Inspect available routes:

```bash
python ../route-pricing/routes.py
```

---

Docs: https://docs.bridgexapi.io
