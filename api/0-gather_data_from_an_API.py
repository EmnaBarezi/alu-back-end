#!/usr/bin/python3
"""
Gather data from a REST API
"""

import requests
import sys


def gather_data(employee_id):
    """Fetch and display TODO list progress"""

    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee data
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    username = user.get("name")

    # Get TODO list
    todos = requests.get(f"{base_url}/todos", params={
        "userId": employee_id
    }).json()

    total_tasks = len(todos)

    done_tasks = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{})".format(
        username,
        len(done_tasks),
        total_tasks
    ))

    # Print completed tasks titles
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        gather_data(int(sys.argv[1]))
