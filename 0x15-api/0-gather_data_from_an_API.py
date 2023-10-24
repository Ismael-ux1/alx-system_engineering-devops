#!/usr/bin/python3
""" REST API script for employee TODO list progress. """
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Define the URL for the REST API
    base_url = 'https://jsonplaceholder.typicode.com'
    endpoint = f'/todos?userId={employee_id}'
    url = base_url + endpoint

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        todos = response.json()

        # Count the number of completed and total tasks
        completed_tasks = [task for task in todos if task['completed']]
        total_tasks = len(todos)

        # Fetch the employee's name
        user_url = base_url + f'/users/{employee_id}'
        user_response = requests.get(user_url)
        if user_response.status_code == 200:
            employee_name = user_response.json().get('name', 'Unknown')
        else:
            employee_name = 'Unknown'

        # Display the progress
        msg = (f"Employee {employee_name} is done with tasks "
               f"({len(completed_tasks)}/{total_tasks}):")
        print(msg)

        for task in completed_tasks:
            print(f"\t{task['title']}")

    else:
        print(f"Failed to retrieve data for employee {employee_id}")


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
