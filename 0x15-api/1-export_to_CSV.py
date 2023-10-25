#!/usr/bin/python3
""" REST API script for employee TODO list progress. """
import requests
import sys
import csv


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    user_info = requests.get(f'{base_url}/users/{employee_id}').json()
    todos = requests.get(f'{base_url}/todos?userId={employee_id}').json()

    completed_tasks = [task for task in todos]
    total_tasks = len(todos)
    employee_name = user_info.get('name', 'Unknown')

    # Print the progress to the console
    print(f'Employee {employee_name} is done with tasks'
          f'({len(completed_tasks)}/{total_tasks}):')

    [print(f'\t {task["title"]}') for task in completed_tasks]

    # Export the data to a CSV file
    export_to_csv(employee_id, employee_name, completed_tasks)


def export_to_csv(employee_id, employee_name, completed_tasks):
    filename = f'{employee_id}.csv'
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                      'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in completed_tasks:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
