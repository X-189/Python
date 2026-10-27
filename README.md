**Simple To-Do List App (Python + Tkinter)**

A very easy desktop to-do list for beginners. It has a graphical window with buttons, and it uses only Python's built-in libraries, so there is nothing to install.

## Features

- Add a task
- Mark a task as done (it turns gray)
- Delete a task

Note: tasks are not saved when you close the window. This keeps the code short and easy to understand.

## Project Structure

```
simple_todo_project/
├── simple_todo.py    # the whole program (about 60 lines)
└── README.md         # this file
```

## Requirements

- Python 3.8 or newer
- Tkinter (included with Python on Windows and macOS)

On some Linux systems, install it with:

```
sudo apt install python3-tk
```

## How to Run

1. Open a terminal in the `simple_todo_project` folder.
2. Run:

```
python simple_todo.py
```

(Use `python3 simple_todo.py` on macOS/Linux if `python` does not work.)

## How to Use

| Action | Steps |
|---|---|
| Add a task | Type in the text box, then click **Add Task** |
| Mark a task done | Click the task in the list, then click **Mark Done** |
| Delete a task | Click the task in the list, then click **Delete Task** |

## How the Code Works

The program has two parts: functions that do the work, and widgets that make up the window.

### Part 1: Functions

| Function | What it does |
|---|---|
| `add_task()` | Reads the text box, adds the text to the list, then clears the box. Shows a warning if the box is empty |
| `delete_task()` | Finds the selected task and removes it |
| `mark_done()` | Finds the selected task and changes its color to gray |

### Part 2: Window and widgets

| Widget | Purpose |
|---|---|
| `tk.Tk()` | Creates the main window |
| `tk.Label` | Shows the title text |
| `tk.Entry` | The box where you type a task |
| `tk.Button` | Buttons that run a function when clicked (`command=...`) |
| `tk.Listbox` | The list that displays the tasks |
| `window.mainloop()` | Keeps the window open and listening for clicks |

### Key ideas

- **Widget:** any item in the window, such as a button or text box.
- **`pack()`:** places a widget in the window, one below the other.
- **`command=`:** tells a button which function to run when it is clicked.
- **`curselection()`:** tells you which item in the list is selected.
- **`messagebox`:** shows a small popup message to the user.

## Practice Ideas

1. Change the window title and size.
2. Change the button colors using `bg="lightblue"`.
3. Add a **Clear All** button that uses `listbox.delete(0, tk.END)`.
4. Make the Enter key add a task using `entry.bind("<Return>", lambda e: add_task())`.
5. Save tasks to a text file and load them when the program starts.

## Learning Outcomes

- Creating a window with Tkinter
- Using labels, entry boxes, buttons and list boxes
- Writing simple functions
- Connecting buttons to functions
- Showing messages with popups
