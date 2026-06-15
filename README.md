#  Project Tracker CLI

A Python-based Command-Line Interface (CLI) application for managing users, projects, and tasks in a simulated software development environment.

The system demonstrates Object-Oriented Programming, file persistence, modular design, and automated testing.

---

##  Features

-  Create and manage users
-  Assign projects to users
-  Create tasks under projects
-  Assign contributors to tasks (many-to-many relationship)
-  Persistent storage using JSON files
-  Unit testing with pytest
-  Clean CLI output using Rich
-  Modular architecture (CLI, models, utils separated)

---

##  Project Structure

project_tracker/
│
├── main.py
├── Pipfile
├── Pipfile.lock
│
├── cli/
├── models/
├── utils/
├── data/
└── tests/


---

##  Installation

### 1. Clone the repository

git clone <your-repo-url>
cd project_tracker

## 2. Install dependencies

Using Pipenv:

pipenv install
pipenv shell

## ▶ Running the Application

Show available commands

python main.py

## User Commands

- Add a user

python main.py add-user --name "Ruth" --email "ruth@test.com"

- List users

python main.py list-users

##  Project Commands

- Add a project

python main.py add-project \
--title "CLI Tool" \
--description "Build CLI application" \
--due_date "2026-12-31" \
--user_id 1

- List projects

python main.py list-projects

## Task Commands

- Add a task

python main.py add-task \
--title "Implement CLI" \
--project "CLI Tool"

- Complete a task

python main.py complete-task --title "Implement CLI"

##  Data Storage

All data is stored locally in JSON files:

data/
├── users.json
├── projects.json
└── tasks.json

## Running Tests

Run all tests using pytest:

pytest

## Design Overview

OOP Concepts Used
- Inheritance
Person → User → Admin

- Encapsulation
Private attributes with property decorators

- Polymorphism
Overridden display_info() methods

- Relationships
One-to-many: Users → Projects
One-to-many: Projects → Tasks
Many-to-many: Tasks ↔ Contributors

## Dependencies

rich
python-dateutil
pytest

## Author

Developed as a Python OOP CLI Project for learning software design, testing, and modular architecture.