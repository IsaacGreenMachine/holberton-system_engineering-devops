#!/usr/bin/python3
"""Exports all employee data in JSON format"""
import json
import sys
from urllib import request


def getData():
    """function to get info from html request"""
    allUrl = "https://jsonplaceholder.typicode.com/users"

    with request.urlopen(allUrl) as response:
        loadedResponse = json.loads(response.read().decode('utf-8'))
        with open('todo_all_employees.json', 'w') as f:
            fullDict = {}
            for u in loadedResponse:
                tdUrl = ("https://"
                         "jsonplaceholder.typicode.com"
                         "/users/{}/todos".format(u.get("id")))
                with request.urlopen(tdUrl) as todoResponse:
                    loadTodo = json.loads(todoResponse.read().decode('utf-8'))
                empID = u.get("id")
                employeeName = u.get("name")
                numTasks = len(loadTodo)
                empUsername = u.get("username")
                doneTasks = sum(map(lambda x: x.get("completed"), loadTodo))
                taskList = []
                for task in loadTodo:
                    taskDict = {}
                    taskDict.update({"task": task.get("title")})
                    taskDict.update({"completed": task.get("completed")})
                    taskDict.update({"username": empUsername})
                    taskList.append(taskDict)
                fullDict.update({empID: taskList})
            f.write(json.dumps(fullDict))


if __name__ == "__main__":
    getData()
