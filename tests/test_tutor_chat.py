import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio

async def test_answer_question(async_client: AsyncClient):
    response = await async_client.post(
        "/answer",
        json={"question": "What is inertia?"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert data["answer"] == "this is a good question"

async def test_empty_question(async_client: AsyncClient):
    response = await async_client.post(
        "/answer",
        json={"question": ""}
    )
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert data["answer"] == "this is a good question"

async def test_answer_validation(async_client: AsyncClient):
    # Test missing question field
    response = await async_client.post(
        "/answer",
        json={}
    )
    assert response.status_code == 422

    # Test invalid JSON
    response = await async_client.post(
        "/answer",
        content="invalid json"
    )
    assert response.status_code == 422 