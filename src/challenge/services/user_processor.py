import logging

from challenge.adapters.csv_reader_adapter import (
    AbstractReaderAdapter,
)
from challenge.tasks import create_user_task

logger = logging.getLogger(__name__)


def read_users_from_csv(
    csv_path: str,
    csv_reader_adapter: AbstractReaderAdapter,
) -> list[dict]:
    return csv_reader_adapter.read(csv_path)


def process_user_registration(
    csv_path: str,
    csv_reader_adapter: AbstractReaderAdapter,
) -> None:
    try:
        users_dict = read_users_from_csv(csv_path, csv_reader_adapter)
        for user_dict in users_dict.values():
            user = user_dict.get("user")
            address = user_dict.get("address")
            create_user_task.delay(user, address)
    except BaseException as e:
        logger.error(f"Error processing users: {e}")
