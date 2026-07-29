from database import get_dealer_url_batches, close_connection
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def main():
    try:
        all_batches = []

        for batch in get_dealer_url_batches(batch_size=5):
            all_batches.append(batch)

        output_json_path = BASE_DIR / "dealer_url_batches.json"

        with open(output_json_path, "w", encoding="utf-8") as out_file:
            json.dump(all_batches, out_file, indent=4, ensure_ascii=False)

        print(f"Successfully saved {len(all_batches)} batches.")

    finally:
        close_connection()


if __name__ == "__main__":
    main()
