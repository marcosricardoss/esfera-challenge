import csv

from typing import Any, Dict
from datetime import datetime
from abc import ABC, abstractmethod


class AbstractReaderAdapter(ABC):
    @abstractmethod
    def read(self, file_path) -> list[dict]: ...


class CSVReaderAdapter(AbstractReaderAdapter):
    def read(self, file_path: str) -> Dict[int, Dict[str, Any]]:
        result = {}

        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                user_id = int(row["user_id"])
                created_at = datetime.fromisoformat(row["created_at"])

                user = {
                    "id": user_id,
                    "name": row["name"],
                    "email": row["email"],
                    "created_at": created_at,
                }

                address = {
                    "id": int(row["address_id"]),
                    "street": row["street"],
                    "city": row["city"],
                    "state": row["state"],
                    "zipcode": row["zipcode"],
                    "country": row["country"],
                    "created_at": created_at,
                }

                result[user_id] = {
                    "user": user,
                    "address": address,
                }

        return result
