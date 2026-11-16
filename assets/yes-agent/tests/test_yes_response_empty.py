"""Unit test: agent returns 'Yes' for an empty or blank message."""
import pytest
from unittest.mock import AsyncMock, patch
from langchain_core.messages import AIMessage, HumanMessage


@pytest.mark.asyncio
async def test_yes_response_empty_message():
    """Agent must return 'Yes' even for an empty message."""
    from agent import SampleAgent

    agent = SampleAgent()

    mock_result = {"messages": [HumanMessage(content=""), AIMessage(content="Yes")]}

    with patch.object(agent, "_invoke", new=AsyncMock(return_value=mock_result)):
        response = await agent.invoke("", "test-ctx-empty")

    assert response.status == "completed"
    assert response.message == "Yes"


@pytest.mark.asyncio
async def test_yes_response_whitespace_message():
    """Agent must return 'Yes' for a whitespace-only message."""
    from agent import SampleAgent

    agent = SampleAgent()

    mock_result = {"messages": [HumanMessage(content="   "), AIMessage(content="Yes")]}

    with patch.object(agent, "_invoke", new=AsyncMock(return_value=mock_result)):
        response = await agent.invoke("   ", "test-ctx-whitespace")

    assert response.status == "completed"
    assert response.message == "Yes"
