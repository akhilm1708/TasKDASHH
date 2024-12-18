# TasKDASHH To-Do List Application

This is a simple To-Do list application built with Python using Tkinter for the user interface and interacting with an API to manage tasks. The app allows users to post tasks, get tasks, and increment their priority using an API.

## Project Structure


## File Breakdown:

- **main.py**: 
  - This is the entry point for the program where `create_ui()` is called to start the Tkinter application. It is responsible for initializing the user interface.

- **ui.py**: 
  - Contains the Tkinter user interface code, including the creation of frames, buttons, and handling user input like posting tasks, getting tasks, and incrementing priorities.

- **funcs.py**: 
  - Includes functions that interact with the API, such as `post_task()`, `get_tasks()`, and `increment_priority()`. These functions send requests to the API and handle the responses.

- **requirements.txt**: 
  - Lists the dependencies needed for the project, such as `requests` for API calls and `tkinter` for the GUI.

- **README.md**: 
  - Documentation file that explains the project, its purpose, how to run it, and any dependencies.

## Installation

To run the project, you will need to install the required dependencies. You can do so by running:

```bash
pip install -r requirements.txt
```
```
python main.py
```

