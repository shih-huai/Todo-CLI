# Todo CLI

A small dependency-free Python todo CLI that stores tasks in `tasks.json`.

## Usage

```powershell
python app.py add "Buy milk"
python app.py list
python app.py delete 1
```

## Functions

- `add_task(task: str)`: Adds a non-empty task and saves it to `tasks.json`.
- `list_tasks()`: Prints all saved tasks with 1-based indexes.
- `delete_task(index: int)`: Deletes a task by its 1-based index and saves the updated task list.
