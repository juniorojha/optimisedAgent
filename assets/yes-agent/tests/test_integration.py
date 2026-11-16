"""Integration test: end-to-end agent flow with mocked LLM."""
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from langchain_core.messages import AIMessage, HumanMessage


@pytest.mark.asyncio
async def test_end_to_end_yes_flow():
    """
    Full end-to-end: simulate a user message going through the agent.
    The LLM is mocked to always return 'Yes'.
    No external calls are made — runs fully offline.
    """
    from agent import SampleAgent

    agent = SampleAgent()

    # Simulate the full graph responding with 'Yes'
    mock_result = {
        "messages": [
            HumanMessage(content="Hello, are you there?"),
            AIMessage(content="Yes"),
        ]
    }

    with patch.object(agent, "_invoke", new=AsyncMock(return_value=mock_result)):
        # Test via stream() to cover the full streaming path
        chunks = []
        async for chunk in agent.stream("Hello, are you there?", "integration-ctx"):
            chunks.append(chunk)

    assert len(chunks) >= 2  # at least "Processing..." + final
    final = chunks[-1]
    assert final["is_task_complete"] is True
    assert final["require_user_input"] is False
    assert final["content"] == "Yes"


@pytest.mark.asyncio
async def test_end_to_end_yes_flow_multi_language():
    """Agent replies 'Yes' to a non-English input."""
    from agent import SampleAgent

    agent = SampleAgent()

    mock_result = {
        "messages": [
            HumanMessage(content="Wie geht es Ihnen?"),
            AIMessage(content="Yes"),
        ]
    }

    with patch.object(agent, "_invoke", new=AsyncMock(return_value=mock_result)):
        response = await agent.invoke("Wie geht es Ihnen?", "integration-ctx-de")

    assert response.status == "completed"
    assert response.message == "Yes"


@pytest.mark.asyncio
async def test_end_to_end_multiline_input():
    """Agent replies 'Yes' to a multi-line message."""
    from agent import SampleAgent

    agent = SampleAgent()

    multiline_msg = "Line one\nLine two\nLine three"
    mock_result = {
        "messages": [
            HumanMessage(content=multiline_msg),
            AIMessage(content="Yes"),
        ]
    }

    with patch.object(agent, "_invoke", new=AsyncMock(return_value=mock_result)):
        response = await agent.invoke(multiline_msg, "integration-ctx-ml")

    assert response.status == "completed"
    assert response.message == "Yes"
