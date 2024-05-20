#!/usr/bin/python3
"""
a script that, using this REST API, for a given employee ID, 
returns information about his/her 
TODO list progress.
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com'
    todos_url = base_url + "/user/{}/todos".format(argv[1])
    user_url = base_url + "/users/{}".format(argv[1])
    todos_result = get(todos_url).json()
    name_result = get(user_url).json()

    todos_num = len(todos_result)
    todos_complete = len([todos for todos in todos_result
                         if todos.get("completed")])
    name = name_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todos_complete, todos_num))
    for todos in todos_result:
        if (todos.get("completed")):
            print("\t {}".format(todos.get("title")))
