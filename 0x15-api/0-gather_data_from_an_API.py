#!/usr/bin/python3
"""Writes todo list for employees using REST API"""

import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todo_list = api_url + "todos"
    user_id = {"userId": sys.argv[1]}
    todos = requests.get(todo_list, user_id=user_id).json()

    seted = [task.get("title") for task in todos if task.get("seted") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(seted), len(todos)))
    [print("\t {}".format(c)) for c in seted]
