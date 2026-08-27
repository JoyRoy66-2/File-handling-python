========================================================================
                     CLI FILE MANAGEMENT SYSTEM
========================================================================

ABOUT THE PROJECT
-----------------
This is a lightweight command-line File Management System built using Python.
It provides a safe, interactive terminal interface to handle standard file 
and directory operations (Create, Read, Update, Delete) with built-in safety 
confirmations to prevent accidental overwrites or file deletions.


FEATURES
--------
1. Auto-Listing : Automatically scans and lists all existing files and 
                  subfolders recursively before performing operations.
2. Create File  : Creates a new file with text content while checking if 
                  the file name already exists to prevent accidental loss.
3. Read File    : Displays the full contents of any existing file safely.
4. Update Options: 
   - Rename     : Change an existing file name to a new one.
   - Overwrite  : Replace all existing file content (requires confirmation).
   - Append     : Add new text onto the end of an existing file.
5. Delete File  : Safely removes a file (requires confirmation).
6. Safety Loop  : Features an infinite `while` loop menu with custom 
                  y/n prompt handling and numerical input validation.


TECHNICAL CONCEPTS USED
-----------------------
- Modern Path Handling : Uses Python's native `pathlib.Path` for object-oriented,
                        cross-platform path creation and recursive searches.
- Recursive Globbing   : Employs `Path.rglob('*')` to dynamically scan through all 
                        directories and nested files.
- File Context Manager : Uses `with open()` blocks for safe reading, writing, 
                        and appending without leaving unclosed file handles.
- Error Handling       : Encapsulates filesystem actions within `try-except` 
                        blocks to handle unexpected system errors smoothly.
- Defensive Prompting  : Custom `confirm()` function ensures users explicit 
                        consent before running destructive filesystem commands.


PREREQUISITES
-------------
- Python 3.x installed on your computer.
- No third-party packages required (uses Python's standard libraries `pathlib` and `os`).


HOW TO RUN THE PROJECT
----------------------
1. Place the script file (e.g., `main.py`) inside the target working directory.
2. Open your terminal or command prompt inside that directory.
3. Run the script using:

   python main.py

4. Follow the interactive menu choices (1 to 5) to perform your file tasks.

========================================================================
