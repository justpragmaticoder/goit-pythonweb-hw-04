import asyncio
from pathlib import Path
import shutil
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def read_folder(source_folder: Path, output_folder: Path):
    """
    Asynchronous function to read all files in the source folder and copy them asynchronously.
    """
    tasks = []
    # Recursive traversal of the source folder
    for item in source_folder.rglob('*'):  # Use regular 'for' instead of 'async for'
        if item.is_file():
            tasks.append(copy_file(item, output_folder))

    # Run all tasks asynchronously
    await asyncio.gather(*tasks)


async def copy_file(file_path: Path, output_folder: Path):
    """
    Asynchronous function to copy a file to a subfolder in the target folder based on file extension.
    """
    try:
        # Determine subfolder based on file extension
        extension = file_path.suffix[1:] if file_path.suffix else 'no_extension'
        target_dir = output_folder / extension
        target_dir.mkdir(parents=True, exist_ok=True)

        # Target path for the file
        target_path = target_dir / file_path.name

        # Copy the file
        await asyncio.to_thread(shutil.copy2, file_path, target_path)
        logger.info(f'Copied file {file_path} to {target_path}')

    except Exception as e:
        logger.error(f"Error copying file {file_path}: {e}")


def main():
    # Interactive command-line input
    source_folder = input("Enter the path to the source folder: ").strip()
    output_folder = input("Enter the path to the output folder: ").strip()

    # Initialize paths
    source_folder = Path(source_folder)
    output_folder = Path(output_folder)

    if not source_folder.is_dir():
        logger.error("Source folder not found or is not a directory.")
        return

    if not output_folder.exists():
        output_folder.mkdir(parents=True, exist_ok=True)

    # Run the asynchronous function
    asyncio.run(read_folder(source_folder, output_folder))


if __name__ == "__main__":
    main()