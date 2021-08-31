import json

data = '''
{
  "name" : "Lou",
  "phone" : {
    "type" : "intl",
    "number" : "+41 78 800 92 72"
  },
  "email" : {
    "private" : "yes"
  }
}'''

info = json.loads(data) # turns the json into a py dicitonary

print(info)
print(type(info)) # dict




