from models.task import Task
from utils.storage import load_data, save_data
from utils.logger import logger


def add_task(args):
    tasks = load_data("tasks.json")
    projects = load_data("projects.json")

    task = Task(args.title)
    tasks.append(task.__dict__)

    for p in projects:
        if p["title"] == args.project:
            p.setdefault("tasks", []).append(args.title)

    save_data("tasks.json", tasks)
    save_data("projects.json", projects)

    logger.info("Task created")


def complete_task(args):
    tasks = load_data("tasks.json")

    for t in tasks:
        if t["title"] == args.title:
            t["status"] = "completed"

    save_data("tasks.json", tasks)