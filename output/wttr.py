import requests

city = "Lyon"

url = "https://wttr.in/" + city

querystring = {
    "format":"j1",
}

response = requests.request("GET", url, params=querystring)
print(response.text)