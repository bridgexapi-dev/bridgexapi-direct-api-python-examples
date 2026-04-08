
# BridgeXAPI Direct API Python Examples

Programmable routing for messaging infrastructure.

BridgeXAPI exposes the routing layer behind SMS delivery.

These examples show direct HTTP execution without SDK abstraction.

No SDK. No abstraction.

Only route-level execution.

---

## Overview

This repository contains executable Python scripts that interact directly with BridgeXAPI.

Each script maps 1:1 to a real API surface.

What is exposed:

* route selection (`route_id`)
* pricing before submission
* delivery tracking (`bx_message_id`)
* routing behavior across multiple paths

This is infrastructure usage, not a wrapped client.

---

## First step (required)

Before sending anything, inspect available routes:

```bash
python route-pricing/routes.py
````

Routes are not universal.

Availability and pricing depend on:

* account configuration
* destination prefix
* active inventory

---

## Setup

```bash
pip install -r requirements.txt
copy .env.example .env
notepad .env
```

Required:

* `BRIDGEXAPI_API_KEY`
* `BRIDGEXAPI_TEST_NUMBER`

---

## Start

```bash
python send-one-message/send_one.py
```

---

## Explore

```bash
python route-pricing/routes.py
python estimate-before-send/estimate.py
python route-comparison/compare_routes.py
python send-from-csv/send_from_csv.py
```

---

## Example output

Route comparison:

```text
[Route 1] ACCEPTED
order_id      : 22521
bx_message_id : BX-22521-7b8bc6311ec9a95a
cost          : 0.088

[Route 4] REJECTED
reason        : No pricing available for destination
```

Delivery lookup:

```text
{
  "bx_message_id": "BX-22519-94fc918774ccf6d8",
  "status": "DELIVERED",
  "route_id": 2
}
```

---

## Structure

* `send-one-message/` → single submission
* `estimate-before-send/` → cost calculation
* `delivery-lookup/` → delivery state
* `route-pricing/` → route + pricing surfaces
* `route-comparison/` → multi-route execution
* `send-from-csv/` → batch sending

---

## Notes

* routing is explicit (`route_id`)
* pricing is route-dependent
* delivery is tracked per message (`bx_message_id`)
* vendor message IDs are not exposed

---

BridgeXAPI

Programmable routing for messaging infrastructure.

Docs: [https://docs.bridgexapi.io](https://docs.bridgexapi.io)
Main: [https://bridgexapi.io](https://bridgexapi.io)

