from __future__ import annotations

from typing import Any


def build_executor(agent: Any) -> Any:
    return agent.agent_executor
