#!/usr/bin/python3
"""
Gather data from an API
"""

import sys
import requests


if __name__ == "__main__":
    employee_id = sys.argv[1]

    # Get employee information
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get TODO list
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    number_done = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_done, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))

