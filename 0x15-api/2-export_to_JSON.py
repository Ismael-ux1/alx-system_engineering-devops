#!/usr/bin/python3
""" Python script to export data in the JSON format """
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch user information
    user_info = requests.get(f'{base_url}/users/{employee_id}').json()
    user_id = user_info.get('id', 'Unknown')
    username = user_info.get('username', 'Unknown')

    # Fetch user's completed tasks using userId parameter
    url = f'{base_url}/todos'
    params = {'userId': employee_id}
    todos = requests.get(url, params=params).json()
    completed_tasks = [task['title'] for task in todos if task['completed']]
    total_tasks = len(todos)

    # Export the data to a JSON file
    export_to_json(employee_id, username, todos)


def export_to_json(employee_id, username, todos):
    filename = f'{employee_id}.json'
    with open(filename, mode='w') as json_file:
        # Create a dictionary with the user ID as the key
        # and a list of tasks as the value
        data = {str(employee_id): []}
        for task in todos:
            # Create a dictionary for each task with the required fields
            task_data = {
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            }
            # Append the task data to the list of tasks
            data[str(employee_id)].append(task_data)
        # Write the data to the JSON file with indentation
        json.dump(data, json_file, indent=None)


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
