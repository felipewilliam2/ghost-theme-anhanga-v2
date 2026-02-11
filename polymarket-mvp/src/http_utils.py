import json
import time
import urllib.parse
import urllib.request
from typing import Any, Dict, Optional

DEFAULT_HEADERS = {
    "user-agent": "Mozilla/5.0 (OpenClaw; polymarket-mvp)",
    "accept": "application/json",
}


def get_json(url: str, params: Optional[Dict[str, Any]] = None, *, timeout: int = 30, retries: int = 5, backoff_s: float = 0.8) -> Any:
    if params:
        qs = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
        url = f"{url}?{qs}"

    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=DEFAULT_HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as f:
                raw = f.read().decode("utf-8")
            return json.loads(raw)
        except Exception as e:
            last_err = e
            sleep = backoff_s * (2 ** attempt)
            time.sleep(sleep)

    raise RuntimeError(f"GET failed after {retries} attempts: {url} ({last_err})")
