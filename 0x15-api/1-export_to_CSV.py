#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Get user ID from command line arguments
    user_id = sys.argv[1]

    # API URL for placeholder data
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch to-do list for the user
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Create CSV file and write to it
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write header row
        writer.writerow(["User ID", "Username", "Completed", "Title"])

        # Write to-do list information to CSV
        for t in todos:
            writer.writerow([user_id, username, t.get("completed"), t.get("title")])
