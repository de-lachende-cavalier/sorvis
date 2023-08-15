import argparse
import json
import os
import urllib.request


def load_valid_categories(filename="utils/quickdraw_categories.txt"):
    """Load the list of valid categories from the .txt file."""
    with open(filename, "r") as file:
        return [line.strip() for line in file]


def download_quickdraw_data(category):
    """Download the QuickDraw data for a given category."""
    url = f"https://storage.googleapis.com/quickdraw_dataset/full/simplified/{category}.ndjson"

    def download_progress_hook(count, block_size, total_size):
        """Display and update the download progress."""
        percent = int(count * block_size * 100 / total_size)
        print(f"\r[+] downloading {category} data... {percent}%", end="")
        if percent == 100:
            print("\n[+] download complete!\n")

    urllib.request.urlretrieve(
        url, f"{category}.ndjson", reporthook=download_progress_hook
    )


def clean_ndjson(filename):
    """Clean the .ndjson file to retain only the recognized drawings."""
    processed_data = []

    with open(filename, "r") as file:
        for line in file:
            data = json.loads(line)

            if data.get("recognized", False):
                # no need to make the taks more difficult for the NCA (if humans didn't recognize the drawing, it's probably not very good...)
                drawing_data = data["drawing"]
                processed_data.append(drawing_data)

    with open(filename, "w") as file:
        for drawing in processed_data:
            file.write(json.dumps({"drawing": drawing}) + "\n")


def main():
    parser = argparse.ArgumentParser(description="download and process QuickDraw data.")
    parser.add_argument(
        "category", type=str, help="the category of QuickDraw data to download."
    )
    parser.add_argument(
        "--dir",
        type=str,
        default=".",
        help="directory to save the downloaded data in.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="clean up the .ndjson file to retain only recognized drawings.",
    )
    args = parser.parse_args()

    valid_categories = load_valid_categories()
    if args.category not in valid_categories:
        print(f"'{args.category}' is not a valid category!")
        return

    os.chdir(args.dir)

    download_quickdraw_data(args.category)

    if args.clean:
        print(f"[+] cleaning up {args.category} data...")
        clean_ndjson(f"{args.category}.ndjson")
        print(f"[+] {args.category} data cleaned successfully.")


if __name__ == "__main__":
    main()
