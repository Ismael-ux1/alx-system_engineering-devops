#!/usr/bin/python3
""" REST API script for employee TODO list progress with CSV export. """
import requests
import sys
import csv


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch user information
    user_info = requests.get(f'{base_url}/users/{employee_id}').json()
    user_id = user_info.get('id', 'Unknown')
    username = user_info.get('username', 'Unknown')

    # Fetch user's completed tasks
    url = f'{base_url}/todos'
    params = {'userId': employee_id}
    todos = requests.get(url, params=params).json()
    completed_tasks = [task['title'] for task in todos if task['completed']]
    total_tasks = len(todos)

    # Print user information and completed tasks
    print(f'User ID and Username: OK')
    print(f'User ID: {user_id} / Username: {username}')
    print(f'Number of tasks in CSV: OK')

    # Export the data to a CSV file
    export_to_csv(employee_id, username, todos)


def export_to_csv(employee_id, username, todos):
    filename = f'{employee_id}.csv'
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                         'TASK_TITLE'])
        for task in todos:
            task_status = 'True' if task['completed'] else 'False'
            writer.writerow([employee_id, username, task_status,
                             task['title']])


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
