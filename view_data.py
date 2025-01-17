# filepath: /d:/digitalpass/view_data.py
from app import db, Task

tasks = Task.query.all()
for task in tasks:
    print(f"ID: {task.id}, Number: {task.number}")