# Q4 - Create multiple threads to simulate file downloading using time.sleep().

import threading
import time

# Constants
DOWNLOAD_FILES = [
    "file1.zip",
    "file2.zip",
    "file3.zip"
]

DOWNLOAD_DELAY_SECONDS = 2


def simulate_file_download(
        file_name: str
) -> None:
    """Simulate downloading a file."""

    print(
        f"Starting Download: "
        f"{file_name}"
    )

    time.sleep(
        DOWNLOAD_DELAY_SECONDS
    )

    print(
        f"Finished Download: "
        f"{file_name}"
    )


def simulate_multiple_downloads() -> None:
    """Create multiple download threads."""

    download_threads = []

    for file_name in DOWNLOAD_FILES:

        download_thread = threading.Thread(
            target=simulate_file_download,
            args=(file_name,)
        )

        download_threads.append(
            download_thread
        )

        download_thread.start()

    for download_thread in download_threads:
        download_thread.join()

    print(
        "All downloads completed."
    )


if __name__ == "__main__":
    simulate_multiple_downloads()