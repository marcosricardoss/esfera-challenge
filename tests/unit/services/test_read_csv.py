from challenge.services.user_processor import read_users_from_csv


class FakeCsvReader:
    def read(self, path):
        return {
            "1": {
                "user": {
                    "id": 1,
                    "name": "John",
                    "email": "john@example.com",
                    "created_at": "2023-01-01T00:00:00",
                },
                "address": {
                    "street": "Main St",
                    "city": "Anytown",
                    "state": "CA",
                    "zipcode": "12345",
                    "country": "USA",
                },
            }
        }


def test_read_users_from_csv():
    adapter = FakeCsvReader()
    result = read_users_from_csv("fake.csv", adapter)
    assert isinstance(result, dict)
    assert result["1"]["user"]["name"] == "John"
