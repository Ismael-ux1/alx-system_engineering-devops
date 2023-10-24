#!/usr/bin/python3
""" REST API script for employee TODO list progress. """
import requests
import sys


def main():
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Get the user data by making a GET request to the user endpoint
    user_id = sys.argv[1]  # Assuming sys.argv[1] contains the user ID
    user_info = requests.get(f"{base_url}users/{user_id}").json()

    # Get the user's todos by making a GET request to the todos endpoint
    todos = requests.get(f"{base_url}todos", params={"userId": user_id}).json()

    # Extract completed tasks
    completed_tasks = [task["title"] for task in todos if task["completed"]]

    # Print the user's name and the number of completed tasks
    print(f"{user_info['name']} completed {len(completed_tasks)}/{len(todos)} tasks:")

    # Print the titles of completed tasks
    [print(f"\t{task}") for task in completed_tasks]


if __name__ == "__main__":
    main()
