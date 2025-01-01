import json

f = open("example.json",'r')
data = json.load(f)
print(type(data))  # tra ve 1 dict
f.close()

for employees in data['Employees']:
    for skill in employees['Skills']:
        print(skill)
    for project in employees['Projects']:
        print(project['ProjectName'])