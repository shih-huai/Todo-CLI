import argparse
import json
from pathlib import Path


TASKS_FILE = Path(__file__).with_name("tasks.json")


def _load_tasks() -> list[dict[str, str]]:
    if not TASKS_FILE.exists():
        return []

    try:
        data = json.loads(TASKS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{TASKS_FILE.name} contains invalid JSON") from exc

    if not isinstance(data, list):
        raise ValueError(f"{TASKS_FILE.name} must contain a JSON list")

    for item in data:
        if not isinstance(item, dict) or not isinstance(item.get("task"), str):
            raise ValueError(f"{TASKS_FILE.name} contains an invalid task")

    return data


def _save_tasks(tasks: list[dict[str, str]]) -> None:
    TASKS_FILE.write_text(
        json.dumps(tasks, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def add_task(task: str) -> dict[str, str]:
    task = task.strip()
    if not task:
        raise ValueError("Task cannot be empty")

    tasks = _load_tasks()
    new_task = {"task": task}
    tasks.append(new_task)
    _save_tasks(tasks)
    return new_task


def list_tasks() -> None:
    tasks = _load_tasks()
    if not tasks:
        print("No tasks yet.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['task']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A simple todo CLI.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a task")
    add_parser.add_argument("task", help="Task description")

    subparsers.add_parser("list", help="List tasks")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "add":
            task = add_task(args.task)
            print(f"Added: {task['task']}")
        elif args.command == "list":
            list_tasks()
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
