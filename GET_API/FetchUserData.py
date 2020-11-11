#  api url
import jsonpath
import requests
import json
url = "https://reqres.in/api/users?page=2"

# send  get request
response = requests.get(url)
# print(response.content)
# print(response.headers)

# Parse response to json format
json_response = json.loads(response.text)
print(json_response)

# fetch value using jsonpath  , it will return list
pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])

# compare value with 5
# assert pages[0] == 5




