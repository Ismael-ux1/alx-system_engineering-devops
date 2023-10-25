#!/usr/bin/python3
""" REST API script for employee TODO list progress. """
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    user_info = requests.get(f'{base_url}/users/{employee_id}').json()
    todos = requests.get(f'{base_url}/todos?userId={employee_id}').json() 
    completed_tasks = [task['title'] for task in todos if task['completed']]
    total_tasks = len(todos)
    employee_name = user_info.get('name', 'Unknown')

    print(f'Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):')
    [print(f' {task}') for task in completed_tasks]


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
