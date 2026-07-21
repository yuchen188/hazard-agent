from __future__ import annotations

DEFAULT_MODEL = "gpt-4o-mini"
DEFAULT_TEMPERATURE = 0.2
DEFAULT_LLM_PROVIDER = "openai"


def get_model_config() -> dict:
    return {
        "model": DEFAULT_MODEL,
        "temperature": DEFAULT_TEMPERATURE,
        "provider": DEFAULT_LLM_PROVIDER,
    }
