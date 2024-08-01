import requests

#endpoint = 'https://httpbin.org/status/200'
#endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'

#get_responsce = requests.get(endpoint) # Application Programming interface

# we can also pass in our own json data to the requests, if you want to use json we can just think of an python Dict 
get_response = requests.get(endpoint, params={'abc': 123},json = {'query':'Hello World'})
# it will just echo back the dict that we pass
# we can also send it as an raw data just replace 'json' with 'data' it will consider as a form in the outPut

#print(get_response.text)
#print(get_response.status_code) # -> 2nd Chapter in the Series

# where we can also get the json 

print(get_response.json())

# there's also a status code that is used to know the out like error code ( 404 like this )


# Rest Api -> is for an Web based Api it uses the HTTP Requests
# This is how we can get the python to scrap the web andget the content from the web

# HTTP Request ->  gives the HTML content
# But the REST API Request which is still ( HTTP ) REST API HTTP Request -> this gives Json(xml) responsce


"""{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.32.3",
    "X-Amzn-Trace-Id": "Root=1-66ab0584-56b75c417a9130a77bb41e50"
  },
  "json": null,
  "method": "GET",
  "origin": "106.51.127.45",
  "url": "https://httpbin.org/anything"
}"""

# This is just like the python Dict but its not 
# JavaScript Object Notation