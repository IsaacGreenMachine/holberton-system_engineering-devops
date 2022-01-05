#!/usr/bin/python3
import json
import sys
from urllib import request
"""returns information about employee progress"""


def getData(empID):
    """function to get info from html request"""
    tdUrl = "https://jsonplaceholder.typicode.com/users/{}/todos".format(empID)
    userUrl = "https://jsonplaceholder.typicode.com/users/{}".format(empID)
    with request.urlopen(tdUrl) as todoResponse:
        with request.urlopen(userUrl) as response:
            loadedTodo = json.loads(todoResponse.read())
            loadedResponse = json.loads(response.read())
            employeeName = loadedResponse.get("name")
            numTasks = len(loadedTodo)
            doneTasks = sum(map(lambda x: x.get("completed"), loadedTodo))
            print("Employee {} is done with tasks({}/{}):".format(
                employeeName,
                doneTasks,
                numTasks))
            for task in loadedTodo:
                if task.get("completed"):
                    print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    getData(sys.argv[1])
