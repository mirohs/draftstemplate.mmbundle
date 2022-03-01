#!/opt/local/bin/python3

# testing without MailMate:
# cat test_input.txt | MM_BUNDLE_SUPPORT=`pwd` ./helper.py

# https://docs.python.org/3/library/index.html
import os
import sys
import json
import csv

# print(os.environ, file=sys.stderr)

path = os.environ["MM_BUNDLE_SUPPORT"] + "/../"
logger = open(path + "log.txt", "w")

def log(msg):
    logger.write(str(msg) + "\n")

# log body
log(sys.stdin.read())

# log environment variables
log(os.environ)

variables = []
with open(path + 'variables.txt', newline='') as csvfile:
    r = csv.reader(csvfile, delimiter='\t')
    header = next(r)
    log(header)
    for row in r:
        kv = {}
        for i in range(len(row)):
            kv[header[i]] = row[i]
        variables.append(kv)
log(variables)

actions = {
    "actions": [{"type": "copyMessage", "variables": v} for v in variables]
}

# actions = {
#     "actions":
#         [
#             {
#                 "type": "copyMessage",
#                 "variables": {
#                     "to": "test@example.com", 
#                     "firstname": "Test",
#                 },
#             },
#         ]
# }

print(json.dumps(actions))

logger.close()
