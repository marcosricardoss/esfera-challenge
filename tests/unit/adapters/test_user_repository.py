import pytest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from challenge.models import Base, User, UserEvent
from challenge.adapters.repository import UserRepository


@pytest.fixture(scope="function")
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    clear_mappers()


def test_user_repository_adds_user_and_event(session):
    # GIVEN
    user_data = {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "created_at": datetime(2023, 5, 5, 6, 40, 54),
    }
    repo = UserRepository(session)
    user = User(**user_data)

    # WHEN
    repo.add(user)
    session.commit()

    # THEN
    user_in_db = session.query(User).filter_by(email="alice@example.com").one()
    assert user_in_db.name == "Alice"

    event = session.query(UserEvent).filter_by(user_id=1).one()
    assert event.event_type == "UserCreated"
    assert event.timestamp == user.created_at

    # WHEN
    user = repo.get_by_email("alice@example.com")

    # THEN
    assert user.name == "Alice"
