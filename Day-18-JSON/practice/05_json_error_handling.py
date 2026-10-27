import json
from pathlib import Path

FILE_PATH = Path("data.json")


def read_json():
    try:
        with FILE_PATH.open("r", encoding="utf-8") as file:
            data = json.load(file)

        print("JSON loaded successfully:")
        print(data)

    except FileNotFoundError:
        print("Error: JSON file not found.")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")

    except OSError as error:
        print("File error:", error)


read_json()
