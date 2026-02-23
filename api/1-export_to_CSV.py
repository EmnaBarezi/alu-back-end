#!/usr/bin/python3
"""
Export employee TODO list data to CSV format
"""

import csv
import requests
import sys


def export_to_csv(employee_id):
    """Export all tasks of an employee to CSV"""

    base_url = "https://jsonplaceholder.typicode.com"

    # Get user data
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    username = user.get("username")

    # Get TODO list
    todos = requests.get(
        f"{base_url}/todos",
        params={"userId": employee_id}
    ).json()

    filename = f"{employee_id}.csv"

    # Write CSV file
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_to_csv(int(sys.argv[1]))
