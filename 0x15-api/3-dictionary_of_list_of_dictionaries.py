#!/usr/bin/python3
""" Python script to export data in the JSON format """
import json
import requests
import sys


def get_all_employees_todo_progress():
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch all users information
    users = requests.get(f'{base_url}/users').json()

    # Fetch all todos information
    todos = requests.get(f'{base_url}/todos').json()

    # Export the data to a JSON file
    export_to_json(users, todos)


def export_to_json(users, todos):
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as json_file:
        # Create an empty dictionary to store the data
        data = {}
        # Loop through the users list
        for user in users:
            # Get the user ID and username
            user_id = user['id']
            username = user['username']
            # Create a list to store the tasks of this user
            tasks = []
            # Loop through the todos list and filter by user ID
            for todo in todos:
                if todo['userId'] == user_id:
                    # Create a dictionary for each task
                    task_data = {
                        "username": username,
                        "task": todo['title'],
                        "completed": todo['completed']
                    }
                    # Append the task data to the list of tasks
                    tasks.append(task_data)
            # Add the user ID and the list of tasks to the data dictionary
            data[str(user_id)] = tasks
        # Write the data to the JSON file with indentation
        json.dump(data, json_file, indent=None)


if __name__ == '__main__':
    get_all_employees_todo_progress()
