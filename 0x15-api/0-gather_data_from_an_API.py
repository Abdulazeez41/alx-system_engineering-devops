#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

# Importing necessary modules
import requests
import sys

# Checking if the script is being run as the main program
if __name__ == "__main__":
    # URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetching user information based on the provided employee ID
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()

    # Fetching to-do list for the specified user
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    # Extracting completed tasks
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Displaying results
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Printing completed tasks with indentation
    [print("\t {}".format(c)) for c in completed]
