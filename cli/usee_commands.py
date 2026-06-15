from models.user import User
from utils.storage import load_data, save_data
from utils.logger import logger


def add_user(args):
    users = load_data("users.json")

    user = User(args.name, args.email)
    users.append(user.__dict__)

    save_data("users.json", users)
    logger.info("User created")


def list_users(_):
    users = load_data("users.json")
    return users