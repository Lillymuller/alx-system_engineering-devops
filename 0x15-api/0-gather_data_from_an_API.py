#!/usr/bin/python3
"""write todo list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos_url = url + "todos"
    params = {"userId": sys.argv[1]}
    todos = requests.get(todos_url, params=params).json()

    completed = [task.get("title") for task in todos if task.get("comp") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
