from __future__ import annotations

from app.agent import HazardReportAgent


def test_agent_can_run_basic_query() -> None:
    agent = HazardReportAgent()
    response = agent.run("某化工厂反应釜区域存在可燃气体泄漏隐患")
    assert "risk_analysis" in response
    assert "inspection_methods" in response
    assert "regulatory_basis" in response
    assert "corrective_actions" in response
