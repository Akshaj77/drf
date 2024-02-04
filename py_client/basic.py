import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint,json={"title":"Hello world"}) #HTTP Request
# print(get_response.text) #print raw text response

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# print(get_response.text) #-> json 
# print(get_response.status_code)
print(get_response.json()) #->python dict

