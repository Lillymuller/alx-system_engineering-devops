#!/usr/bin/python3
"""Exports todo list for a given employee to CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos_url = url + "todos"
    params = {"userId": user_id}
    todos = requests.get(todos_url, params=params).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, task.get("completed"), task.get("title")]
         ) for task in todos]
