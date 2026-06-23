# Simple TASKS

A Simple TASK manager written in Python. This project allows users to create, view, complete, and remove tasks while storing them in text files so that data persists between sessions.

## Features

* View current tasks
* View completed tasks
* Add new tasks
* Mark tasks as completed
* Remove tasks
* Persistent data
* Simple menu for easy navigation

## Project Structure

```text
Simple-TASKS/
│
├── main.py
├── README.md
├── LICENSE
└── Tasks/
    ├── tasks.txt
    └── completedtasks.txt
```


## How to Run

1. Clone the repository:

```bash
git clone https://github.com/notmasked/Simple-TASKS.git
```

2. Navigate to the project directory:

```bash
cd python-task-manager
```

3. Run the program:

```bash
python main.py
```

## Example

```
■-- Welcome to TASKS! --■

1. View Tasks
2. Complete Tasks
3. Add Tasks
4. Remove Tasks
5. Exit
```

## Technologies Used

* Python 3
* File Handling
* Functions
* String Manipulation

## Future plans for updates

* Input validation with try/except
* Replace recursive menus with loops
* Prevent duplicate tasks
* Task priorities
* Due dates
* JSON-based storage
* GUI version using Tkinter

## Author

Harshad Sawant

## License

This project is open source and available under the MIT License.
