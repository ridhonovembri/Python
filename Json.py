import json

#some of json
json_data = '{"name":"ridho","age":"30"}'

#parse json to python
cFromjsontoPy = json.loads(json_data)
print(cFromjsontoPy)
print(cFromjsontoPy["name"])
print(cFromjsontoPy["age"])

#some of dict data from python
dict_data = {
    "name":"icha",
    "age":"7"
}

#parse python dict to json
cFromPythontoJson = json.dumps(dict_data)
print(cFromPythontoJson)

