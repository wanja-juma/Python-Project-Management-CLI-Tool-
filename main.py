import argparse

from cli.user_commands import add_user, list_users
from cli.project_commands import add_project, list_projects
from cli.task_commands import add_task, complete_task

from utils.helpers import print_table


def main():
    parser = argparse.ArgumentParser(description="Project Tracker CLI")

    subparsers = parser.add_subparsers(dest="command")

   
    # USER COMMANDS
    
    add_user_cmd = subparsers.add_parser("add-user")
    add_user_cmd.add_argument("--name", required=True)
    add_user_cmd.add_argument("--email", required=True)
    add_user_cmd.set_defaults(func=add_user)

    list_users_cmd = subparsers.add_parser("list-users")
    list_users_cmd.set_defaults(func=list_users)

    
    # PROJECT COMMANDS
   
    add_project_cmd = subparsers.add_parser("add-project")
    add_project_cmd.add_argument("--title", required=True)
    add_project_cmd.add_argument("--description", required=True)
    add_project_cmd.add_argument("--due_date", required=True)
    add_project_cmd.add_argument("--user_id", required=True)
    add_project_cmd.set_defaults(func=add_project)

    list_projects_cmd = subparsers.add_parser("list-projects")
    list_projects_cmd.set_defaults(func=list_projects)

    
    # TASK COMMANDS
    
    add_task_cmd = subparsers.add_parser("add-task")
    add_task_cmd.add_argument("--title", required=True)
    add_task_cmd.add_argument("--project", required=True)
    add_task_cmd.set_defaults(func=add_task)

    complete_task_cmd = subparsers.add_parser("complete-task")
    complete_task_cmd.add_argument("--title", required=True)
    complete_task_cmd.set_defaults(func=complete_task)

    # PARSE ARGS
    
    args = parser.parse_args()

    # SAFE EXECUTION 
    if hasattr(args, "func"):
        args.func(args)
    else:
        print("\n No command provided.\n")
        parser.print_help()


if __name__ == "__main__":
    main()