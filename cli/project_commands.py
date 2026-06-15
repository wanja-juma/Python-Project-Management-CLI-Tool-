from models.project import Project
from utils.storage import load_data, save_data
from utils.logger import logger


def add_project(args):
    projects = load_data("projects.json")
    users = load_data("users.json")

    project = Project(args.title, args.description, args.due_date, args.user_id)
    projects.append(project.__dict__)

    for u in users:
        if str(u["id"]) == str(args.user_id):
            u.setdefault("projects", []).append(args.title)

    save_data("projects.json", projects)
    save_data("users.json", users)

    logger.info("Project created")


def list_projects(_):
    return load_data("projects.json")