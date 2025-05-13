import logging
import sqlalchemy.exc

from datetime import datetime
from celery import shared_task

from challenge.models import User, Address
from challenge.services.unit_of_work import SqlAlchemyUnitOfWork
from challenge.config import RATE_LIMIT

logger = logging.getLogger(__name__)


@shared_task
def user_created_event(user_id: int, email: str):
    logger.info(f"UserCreated event received: ID={user_id}, Email={email}")


@shared_task(rate_limit=RATE_LIMIT)
def create_user_task(user_data: dict, address_data: dict):
    uow = SqlAlchemyUnitOfWork()

    try:
        with uow:
            address = Address(
                street=address_data["street"],
                city=address_data["city"],
                state=address_data["state"],
                zipcode=address_data["zipcode"],
                country=address_data["country"],
            )

            user = User(
                id=user_data["id"],
                name=user_data["name"],
                email=user_data["email"],
                created_at=datetime.fromisoformat(str(user_data["created_at"])),
                address=address,
            )

            uow.users.add(user)
            uow.commit()
            user_created_event.delay(user.id, user.email)

    except sqlalchemy.exc.IntegrityError:
        logger.error(f"User {user_data['id']} already exists")
        uow.rollback()
    except Exception as e:
        logger.error(f"Unexpected error for user {user_data['id']}: {e}")
        uow.rollback()
