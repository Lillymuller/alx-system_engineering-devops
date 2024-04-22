#!/usr/bin/python3
"""Writes todo list for employees using REST API"""

import requests
import sys

""" Retrieves and displays an employee's TODO list progress from a REST API
Args:
employee_id (int): The ID of the employee.
"""

if __name__ == "__main__":

    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo_list = requests.get(url + "todo_list", user_id={"userId": sys.argv[1]}).json()

    seted = [t.get("title") for t in todo_list if t.get("seted") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(seted), len(todo_list)))
    [print("\t {}".format(c)) for c in seted]
