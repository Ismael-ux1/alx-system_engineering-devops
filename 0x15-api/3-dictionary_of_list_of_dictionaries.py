#!/usr/bin/python3
import requests
import json
""" Python script to export data in the JSON format. """


def fetch_user_tasks(user_id):
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Get the user data by making a GET request to the user endpoint
    user_info = requests.get(f"{base_url}users/{user_id}").json()

    # Get the user's todos by making a GET request to the todos endpoint
    todos = requests.get(f"{base_url}todos", params={"userId": user_id}).json()

    # Extract completed tasks for the user
    completed_tasks = [{"username": user_info["name"], "task": task["title"], "completed": task["completed"]} for task in todos]

    return user_id, completed_tasks


def main():
    all_user_tasks = {}

    # List of user IDs, you can add or change IDs as needed
    user_ids = [1, 2, 3, 4, 5]  # Example user IDs

    for user_id in user_ids:
        user_id, completed_tasks = fetch_user_tasks(user_id)
        all_user_tasks[user_id] = completed_tasks

    # Export all user tasks to a JSON file
    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(all_user_tasks, json_file, indent=4)


if __name__ == "__main__":
    main()
