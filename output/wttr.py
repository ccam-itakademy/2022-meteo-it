import requests
import json

city = "Lyon"

url = "https://wttr.in/" + city

querystring = {
    "format":"j1",
}

response = requests.request("GET", url, params=querystring)
print(response.text)

json.dump(city)

#Envoyer dans un fichier la réponse
#Py -> php