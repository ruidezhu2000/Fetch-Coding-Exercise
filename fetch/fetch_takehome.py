# Author: Ruide Zhu
# Date: 02/01/2023

import csv
import sys
import collections
import json

# function used to find points balances after points are spent
def findBalance():

    # take wanted points input and use 5000 if no points entered
    if len(sys.argv) < 2:
        print("Points input needed!\nDefault points 5000 used")
        points = 5000
    else:
        points = int(sys.argv[1])

    # read and process transactions.csv
    data = []
    try:
        with open('transactions.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
    except:
        print("File not found!")
        return
    data = data[1:]
    data.sort(key=lambda x: x[2])

    # dealing with balance update while we have points to spend
    users = collections.defaultdict(int)
    idx = 0
    while idx < len(data):
        user, point, _ = data[idx]
        point = int(point)
        if points <= 0:
            break
        if point >= 0:
            users[user] += point
            points -= point
            if points < 0:
                users[user] -= point+points
            else:
                users[user] -= point
        else:
            points -= point
        idx += 1

    # dealing with balance update while we do not have points to spend
    while idx < len(data):
        user, point, _ = data[idx]
        point = int(point)
        users[user] += point
        idx += 1

    # convert to json object and return the result
    return json.dumps(users, indent=4)


if __name__ == "__main__":
    print(findBalance())
