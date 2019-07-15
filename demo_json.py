import json

# some JSON:
json_string = '''
{
    "routingprotocol": [
        {
            "name": "EIGRP",
            "invented": 1993,
            "multicast": "224.0.0.10"
        },
        {
            "name": "OSPFv3",
            "invented": 2008,
            "multicast": ["224.0.0.5", "224.0.0.6"]
        },
        {
            "name": "RIPv2",
            "invented": 1993,
            "multicast": "224.0.0.9"
        }
    ]
}
'''

print("-------------------------------------------------------------------")
print("Onderstaande is een string in json structuur ",type(json_string))
print("-------------------------------------------------------------------")
print(json_string)


#create dict from json string
json_dict = json.loads(json_string)
print("-------------------------------------------------------------------")
print("Met json.loads(json_string) maak je er een dict van",type(json_dict))
print("-------------------------------------------------------------------")
print("")

# the result is a Python dictionary:
print("-------------------------------------------------------------------")
print(json_dict)
print("-------------------------------------------------------------------")
print(json_dict["routingprotocol"])
print("-------------------------------------------------------------------")
print(json_dict["routingprotocol"][1])
print("-------------------------------------------------------------------")
print(json_dict["routingprotocol"][0]["name"])
print("-------------------------------------------------------------------")
print(json_dict["routingprotocol"][2]["multicast"])
print("-------------------------------------------------------------------")
print(json_dict["routingprotocol"][1]["multicast"][1])
print("-------------------------------------------------------------------")


#Een string is een string met zijn beperkingen
#print(json_string["routingprotocol"])


