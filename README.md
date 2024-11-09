# File Sorter Script

This Python script sorts files in a specified source folder into subfolders based on their file extensions, placing them in an output directory. It uses asynchronous operations to handle large volumes of files efficiently.

## How to Use

### Run `main.py`

You can run the script using one of the following commands (depending on your python version and existence of pyenv):

```bash
python3 main.py
```
```bash
pyenv exec python main.py
```

### Enter the Source Folder Path

When prompted, provide the path to the folder containing the files to be sorted.
Example:

```bash
./test_folder
```

### Enter the Output Folder Path

```bash
.
```

## Requirements

- **Python 3.7+**  
  Ensure you have Python version 3.7 or higher installed.

- **asyncio**  
  A built-in library for asynchronous operations (available with Python 3.7+).

- **shutil**  
  A built-in library for file operations.

## Logging and Errors

The script provides detailed logging for each file operation:
- Each file copied is logged with its source and target paths.
- Any errors encountered during file operations are recorded.

You can review all log messages in the console output for easy debugging and tracking of file processing.