from __future__ import annotations

import time
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def timed_block() -> Iterator[None]:
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"elapsed={elapsed:.3f}s")
