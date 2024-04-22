#!/usr/bin/python3
"""
Write a sript using REST API that returns employees todo list
Requirements:
    You must use urllib or requests module
    EMPLOYEE_NAME: name of the employee
    NUMBER_OF_DONE_TASKS: number of completed tasks
    TOTAL_NUMBER_OF_TASKS: total number of tasks
Second and N next lines display the title of completed tasks
"""

import urllib.request
import requests
import sys


if __name__ == "__main__":
    api_ url = "https://jsonplaceholder.typicode.com/"
    
    """Fetch user data"""
    user_url = url + "users/{}".format(sys.argv[1])
    with urllib.request.urlopen(user_url) as response:
        user_data = json.loads(response.read().decode())

    """Fetch todos data with parameters"""
    todo_list = url + "todos"
    user_id = {"userId": sys.argv[1]}
    encoded_params = urllib.parse.urlencode(user_id).encode()
    with urllib.request.urlopen(todo_list, encoded_params) as response:
        todos_data = json.loads(response.read().decode())

    """Filter completed tasks"""
    seted = [todo.get("title") for todo in todos_data
            if todo.get("completed") is True]

    """Print summary"""
    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), len(seted), len(todos_data)))

    """Print individual completed tasks"""
    [print("\t {}".format(c)) for c in seted]
