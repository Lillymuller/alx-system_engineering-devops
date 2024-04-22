#!/usr/bin/python3
"""Writes todo list for employees using REST API"""

import requests

def get_todo_progress(employee_id):
  """
  Retrieves and displays an employee's TODO list progress from a REST API.

  Args:
    employee_id (int): The ID of the employee.
  """
  url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
  params = {"_expand": "todos"}  # Include related todos

  try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise exception for non-200 status codes

    data = response.json()
    user_name = data.get("name")
    todos = data.get("todos", [])

    completed_tasks = [todo for todo in todos if todo["completed"]]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    print(f"Employee {user_name} is done with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
      print(f"\t {task['title']}")

  except requests.exceptions.RequestException as e:
    print(f"Error: Failed to retrieve data: {e}")

if __name__ == "__main__":
  try:
    employee_id = int(input("Enter employee ID: "))
    get_todo_progress(employee_id)
  except ValueError:
    print("Error: Invalid employee ID (must be an integer).")
