from challenge.adapters.csv_reader_adapter import CSVReaderAdapter
from challenge.services.user_processor import process_user_registration

FILE = "/opt/app/usuarios.csv"


def main():  # pragma: no cover
    process_user_registration(FILE, csv_reader_adapter=CSVReaderAdapter())


if __name__ == "__main__":
    main()
