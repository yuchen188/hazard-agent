from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi import FastAPI
from pydantic import BaseModel

from app.agent import HazardReportAgent

app = FastAPI(title="Hazard Report Agent")
agent = HazardReportAgent()


class GenerateReportRequest(BaseModel):
    query: str


class GenerateReportResponse(BaseModel):
    query: str
    answer: dict


@app.post("/generate-report", response_model=GenerateReportResponse)
def generate_report(request: GenerateReportRequest) -> GenerateReportResponse:
    answer = agent.run(request.query)
    return GenerateReportResponse(query=request.query, answer=answer)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
