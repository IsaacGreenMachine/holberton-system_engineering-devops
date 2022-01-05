#!/usr/bin/python3
"""exports data from task 0 in JSON format"""
import csv
import json
import sys
from urllib import request


def getData(empID):
    """function to get info from html request"""
    tdUrl = "https://jsonplaceholder.typicode.com/users/{}/todos".format(empID)
    userUrl = "https://jsonplaceholder.typicode.com/users/{}".format(empID)
    with request.urlopen(tdUrl) as todoResponse:
        with request.urlopen(userUrl) as response:
            loadedTodo = json.loads(todoResponse.read().decode('utf-8'))
            loadedResponse = json.loads(response.read().decode('utf-8'))
            employeeName = loadedResponse.get("name")
            numTasks = len(loadedTodo)
            empUsername = loadedResponse.get("username")
            doneTasks = sum(map(lambda x: x.get("completed"), loadedTodo))
            with open('{}.json'.format(empID), 'w') as f:
                taskList = []
                for task in loadedTodo:
                    taskDict = {}
                    taskDict.update({"task": task.get("title")})
                    taskDict.update({"completed": task.get("completed")})
                    taskDict.update({"username": empUsername})
                    taskList.append(taskDict)
                fullDict = {}
                fullDict.update({empID: taskList})
                f.write(json.dumps(fullDict))


if __name__ == "__main__":
    getData(sys.argv[1])
