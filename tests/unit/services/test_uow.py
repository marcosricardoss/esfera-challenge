# tests/test_uow.py

from challenge.services.unit_of_work import SqlAlchemyUnitOfWork
from challenge.adapters.repository import UserRepository


class FakeSession:
    def __init__(self):
        self.committed = False
        self.rolled_back = False
        self.closed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        self.rolled_back = True

    def close(self):
        self.closed = True


class FakeUserRepository:
    def __init__(self, session):
        self.session = session


def test_sqlalchemy_uow_commit_and_close(monkeypatch):
    session = FakeSession()

    monkeypatch.setattr(
        "challenge.adapters.repository.UserRepository", FakeUserRepository
    )

    uow = SqlAlchemyUnitOfWork(session_factory=lambda: session)

    with uow as u:
        assert isinstance(u.users, UserRepository)
        u.commit()
        assert session.committed is True

    assert session.closed is True


def test_sqlalchemy_uow_rollback(monkeypatch):
    session = FakeSession()
    monkeypatch.setattr(
        "challenge.adapters.repository.UserRepository", FakeUserRepository
    )

    uow = SqlAlchemyUnitOfWork(session_factory=lambda: session)

    try:
        with uow:
            raise Exception("Test error")
    except Exception:
        pass

    assert session.rolled_back is True
    assert session.closed is True
