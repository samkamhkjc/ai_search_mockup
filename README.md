# Search Demo (Google-like)

A static web demo that mimics Google’s search page and results, with a **dropdown** for queries, **static JSON** data, and an optional **AI Overview** (RAG-style) on the results page.

## Features

- **Search page** – Google-style layout with logo, query dropdown, and “AI Overview” checkbox
- **Results page** – Result list plus optional AI Overview block at the top when the mode is on
- **Dropdown** – Query chosen from a list (no free-text input)
- **Static JSON** – All results come from `data/demo-results.json`
- **AI Overview** – If “AI Overview” is enabled, the results page shows an overview paragraph above the links; otherwise only the normal result list is shown

## Run locally

The app must be served over HTTP so `fetch()` can load `data/demo-results.json` (avoids `file://` CORS issues).

**Python 3** (use `py` on Windows if `python` is not recognized; this project includes `python.cmd` so `python` is equivalent to `py` when run from the project directory):
```bash
cd c:\Users\HKJCUser\PycharmProjects\ai_search_demo_cursor
python -m http.server 8000
```
or on Windows:
```bash
py -m http.server 8000
```

**Node (npx)** — if Python is not available:
```bash
cd c:\Users\HKJCUser\PycharmProjects\ai_search_demo_cursor
npx serve -p 8000
```

Then open: **http://localhost:8000**

## Files

| File | Role |
|------|------|
| `index.html` | Search home: dropdown, “AI Overview” checkbox, Demo Search / I’m Feeling Lucky |
| `results.html` | Results: optional AI Overview block and result list from JSON |
| `data/demo-results.json` | Demo data: `queryOptions` (for the dropdown) and `data` (per-query `aiOverview` + `results`) |
| `css/style.css` | Shared styles for both pages |
| `js/app.js` | `loadDemoData()` to fetch the JSON |

## JSON format

- **`queryOptions`**: `[{ "id": "...", "label": "..." }]` for the dropdown.
- **`data`**: `{ "<id>": { "aiOverview": "optional RAG-style text", "results": [{ "title", "url", "snippet" }] } }`.

If `aiOverview` is present and the user turned on “AI Overview”, it is shown in the top block on the results page.
