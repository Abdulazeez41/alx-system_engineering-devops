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

    # API URL for JSONPlaceholder
    url = "https://jsonplaceholder.typicode.com/"

    # Get user information using the provided user ID
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract username from user information
    username = user.get("username")

    # Get to-do list for the specified user ID
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Open a CSV file for writing
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        # Create a CSV writer
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write CSV header
        writer.writerow(["User ID", "Username", "Completed", "Title"])

        # Write each to-do item to the CSV file
        [writer.writerow([user_id, username, t.get("completed"), t.get("title")]) for t in todos]
