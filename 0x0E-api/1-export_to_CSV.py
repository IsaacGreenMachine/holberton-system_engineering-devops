#!/usr/bin/python3
"""exports data from task 0 in CSV format"""
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
            with open('{}.csv'.format(empID), 'w') as f:
                csvwriter = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
                for task in loadedTodo:
                    csvwriter.writerow([task.get("userId"),
                                        empUsername,
                                        task.get("completed"),
                                        task.get("title")])


if __name__ == "__main__":
    getData(sys.argv[1])
