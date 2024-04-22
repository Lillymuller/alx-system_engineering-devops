#!/usr/bin/python3
"""Writes todo list for employees using REST API"""

import requests
import sys

if __name__ == "__main__":

    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todo_list = requests.get(api_url + "todo_list", user_id={"userId": sys.argv[1]}).json()

    seted = [x.get("title") for x in todo_list if x.get("seted") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(seted), len(todo_list)))
    [print("\t {}".format(c)) for c in seted]
