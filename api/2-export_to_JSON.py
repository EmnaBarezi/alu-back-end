#!/usr/bin/python3
"""
Export employee TODO list data to JSON format
"""

import json
import requests
import sys


def export_to_json(employee_id):
    """Export all tasks of an employee into JSON file"""

    base_url = "https://jsonplaceholder.typicode.com"

    # Get user info
    user = requests.get(
        f"{base_url}/users/{employee_id}"
    ).json()

    username = user.get("username")

    # Get TODO list
    todos = requests.get(
        f"{base_url}/todos",
        params={"userId": employee_id}
    ).json()

    # Build JSON structure
    task_list = []

    for task in todos:
        task_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {
        str(employee_id): task_list
    }

    # Write JSON file
    filename = f"{employee_id}.json"

    with open(filename, "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_to_json(int(sys.argv[1]))
