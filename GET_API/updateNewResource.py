import json

import jsonpath
import requests

# API url
url = "https://reqres.in/api/users/2"

# read input file json
file = open('C:\\Users\\lappy\\Desktop\\TrulyMadly\\projects\\api\\data.json', 'r')

json_input = file.read()  # this is in form of text although imported data in file was  in json format
print(json_input)

# parse data into json format ---->  converts it in json format
request_json = json.loads(json.dumps(json_input))
print(request_json)

# make put request with json input body
response = requests.put(url, request_json)
print(response)

# validating response code
print(response.status_code)

print(response.headers.get('Content-length'))

# parse response to json format
response_json = json.loads(response.text)
print(response_json)

# pick  id using jsonpath from json response file
updated = jsonpath.jsonpath(response_json,'updatedAt')
print(updated[0])



