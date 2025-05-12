from challenge.adapters.csv_reader_adapter import (
    AbstractReaderAdapter,
    CSVReaderAdapter,
)


def read_users_from_csv(
    csv_path: str,
    csv_reader_adapter: AbstractReaderAdapter = CSVReaderAdapter(),
) -> list[dict]:
    return csv_reader_adapter.read(csv_path)


def process_user_registration(csv_path: str) -> None:
    users_dict = read_users_from_csv(csv_path)
    for user_data in users_dict.values():
        print(user_data)
        # dict to User
        # event ID (UserCreated)
        # log event ID (UserCreated)
