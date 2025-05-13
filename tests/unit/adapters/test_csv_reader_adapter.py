import tempfile
import os
from datetime import datetime

from challenge.adapters.csv_reader_adapter import CSVReaderAdapter


def test_csv_reader_adapter_reads_correctly():
    # GIVEN
    csv_content = """user_id,address_id,name,email,street,city,state,zipcode,country,created_at
1,101,John Doe,john@example.com,123 Main St,Anytown,CA,12345,USA,2023-01-01T10:00:00
"""

    # Cria um arquivo temporário
    with tempfile.NamedTemporaryFile(
        mode="w+", delete=False, suffix=".csv"
    ) as temp_file:
        temp_file.write(csv_content)
        temp_file_path = temp_file.name

    try:
        adapter = CSVReaderAdapter()

        # WHEN
        result = adapter.read(temp_file_path)

        # THEN
        assert 1 in result
        user_data = result[1]["user"]
        address_data = result[1]["address"]

        assert user_data["name"] == "John Doe"
        assert user_data["email"] == "john@example.com"
        assert isinstance(user_data["created_at"], datetime)

        assert address_data["street"] == "123 Main St"
        assert address_data["city"] == "Anytown"
        assert isinstance(address_data["created_at"], datetime)

    finally:
        os.remove(temp_file_path)
