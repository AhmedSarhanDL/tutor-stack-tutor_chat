from unittest.mock import patch


def test_answer_question(client):
    response = client.post(f"{client.base_url}/answer", json={"question": "What is inertia?"})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "confidence" in data
    assert data["answer"] == (
        "This is a test response for the automated PR. In production, this would be "
        "a real tutored answer."
    )
    assert data["confidence"] == 0.95


def test_empty_question(client):
    response = client.post(f"{client.base_url}/answer", json={"question": ""})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "confidence" in data
    assert data["answer"] == (
        "This is a test response for the automated PR. In production, this would be "
        "a real tutored answer."
    )
    assert data["confidence"] == 0.95


def test_answer_validation(client):
    # Test missing question field
    response = client.post(f"{client.base_url}/answer", json={})
    assert response.status_code == 422

    # Test invalid JSON
    response = client.post(
        f"{client.base_url}/answer",
        data="invalid json",
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 422


def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get(f"{client.base_url}/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "healthy"


def test_long_question(client):
    """Test with a longer question to ensure it handles various input lengths"""
    long_question = (
        "What is the relationship between mass, acceleration, and force according to "
        "Newton's second law of motion, and how does this apply to real-world scenarios "
        "like car crashes and rocket propulsion?"
    )
    response = client.post(f"{client.base_url}/answer", json={"question": long_question})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "confidence" in data
    assert isinstance(data["answer"], str)
    assert isinstance(data["confidence"], float)


def test_answer_exception_handling(client):
    """Test the exception handling in the answer endpoint"""
    with patch("tutor_stack_chat.main.Answer") as mock_answer:
        # Make the Answer constructor raise an exception
        mock_answer.side_effect = Exception("Test exception")

        response = client.post(f"{client.base_url}/answer", json={"question": "Test question"})
        assert response.status_code == 500
        data = response.json()
        assert "detail" in data
        assert data["detail"] == "Test exception"
