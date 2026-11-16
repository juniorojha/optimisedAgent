"""Unit test: agent returns 'Yes' for a regular user message."""
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from langchain_core.messages import AIMessage, HumanMessage


@pytest.mark.asyncio
async def test_yes_response_regular_message():
    """Agent must return 'Yes' for a regular user message."""
    from agent import SampleAgent

    agent = SampleAgent()

    # Mock the LangGraph invoke to return a canned 'Yes' response
    mock_result = {"messages": [HumanMessage(content="What is the weather?"), AIMessage(content="Yes")]}

    with patch.object(agent, "_invoke", new=AsyncMock(return_value=mock_result)):
        response = await agent.invoke("What is the weather today?", "test-ctx-1")

    assert response.status == "completed"
    assert response.message == "Yes"


@pytest.mark.asyncio
async def test_yes_response_arbitrary_question():
    """Agent must return 'Yes' for any arbitrary question."""
    from agent import SampleAgent

    agent = SampleAgent()

    mock_result = {"messages": [HumanMessage(content="some question"), AIMessage(content="Yes")]}

    with patch.object(agent, "_invoke", new=AsyncMock(return_value=mock_result)):
        response = await agent.invoke("Tell me the meaning of life", "test-ctx-2")

    assert response.status == "completed"
    assert response.message == "Yes"
