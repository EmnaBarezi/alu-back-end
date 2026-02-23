#!/usr/bin/python3
"""
Gather data from an API
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)

    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_data = requests.get(user_url).json()
    employee_name = user_data.get("name")

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todos_data = requests.get(todos_url).json()

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    number_done = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_done, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))

