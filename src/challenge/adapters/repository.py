from abc import ABC, abstractmethod

from challenge.models import User, UserEvent
from sqlalchemy.orm import Session


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> None: ...


class UserRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, user: User) -> None:
        self.session.add(user)
        self.session.add(
            UserEvent(
                user_id=user.id,
                event_type="UserCreated",
                timestamp=user.created_at,
            )
        )

    def get_by_email(self, email: str) -> User | None:
        return self.session.query(User).filter_by(email=email).first()
