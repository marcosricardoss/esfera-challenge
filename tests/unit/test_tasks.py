import pytest
from unittest.mock import MagicMock, patch

from challenge.tasks import create_user_task, user_created_event


@pytest.fixture
def user_data():
    return {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "created_at": "2023-01-01T10:00:00",
    }


@pytest.fixture
def address_data():
    return {
        "id": 1,
        "user_id": 1,
        "street": "123 Main St",
        "city": "City",
        "state": "State",
        "zipcode": "12345",
        "country": "Country",
    }


def test_user_created_event_logs(caplog):
    with caplog.at_level("INFO"):
        user_created_event(1, "john@example.com")
        assert "UserCreated event received: ID=1, Email=john@example.com" in caplog.text


@patch("challenge.tasks.SqlAlchemyUnitOfWork")
def test_create_user_task_unexpected_error_logs_and_rolls_back(
    mock_uow, user_data, address_data, caplog
):
    mock_repo = MagicMock()
    mock_uow_instance = MagicMock()
    mock_uow_instance.__enter__.return_value = mock_uow_instance
    mock_uow_instance.users = mock_repo
    mock_repo.add.side_effect = Exception("Unexpected error")
    mock_uow.return_value = mock_uow_instance

    with caplog.at_level("ERROR"):
        create_user_task(user_data, address_data)
        assert f"Unexpected error for user {user_data['id']}" in caplog.text
        mock_uow_instance.rollback.assert_called_once()
