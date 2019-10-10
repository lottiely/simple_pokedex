import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon-species/ninetales/")

print(response.status_code)

ninetalesobj = response.json()
flavortext = ""

for x in ninetalesobj["flavor_text_entries"]:
    if():
        

print(ninetalesobj["flavor_text_entries"][0]["flavor_text"])

#for x in ninetalesobj["flavor_text_entries"]:
#    flavortext = x[0].flavor_text

#print(json.dumps(response.json(), indent=2))