#!/usr/bin/python3
"""
Export all employees TODO list data to JSON format
"""

import json
import requests


def export_all_to_json():
    """Export tasks of all employees"""

    base_url = "https://jsonplaceholder.typicode.com"

    # Get users
    users = requests.get(f"{base_url}/users").json()

    # Get todos
    todos = requests.get(f"{base_url}/todos").json()

    # Build username lookup dictionary
    user_dict = {}

    for user in users:
        user_dict[user.get("id")] = user.get("username")

    # Build result structure
    result = {}

    for task in todos:
        user_id = task.get("userId")

        if user_id not in result:
            result[user_id] = []

        result[user_id].append({
            "username": user_dict.get(user_id),
            "task": task.get("title"),
            "completed": task.get("completed")
        })

    # Write JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(result, json_file)


if __name__ == "__main__":
    export_all_to_json()
