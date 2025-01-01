import csv

f = open("example.csv",'r')
data = csv.reader(f) # tra ve danh sach list
data_2 = csv.DictReader(f) # tra ve danh sach cac tu dien

# for row in data:
#     print(row)
# ['EmployeeID', 'Name', 'Department', 'Salary', 'JoinDate']
# ['101', 'John Doe', 'Sales', '50000', '2018-05-12']
# ['102', 'Jane Smith', 'Marketing', '55000', '2019-06-15']
# ['103', 'Emily Davis', 'HR', '60000', '2017-09-23']
# ['104', 'Michael Brown', 'Engineering', '75000', '2020-01-10']
# ['105', 'Linda Wilson', 'Finance', '70000', '2016-11-20']

for row in data_2:
    print(row['Name'])
    print(row)
# {'EmployeeID': '101', 'Name': 'John Doe', 'Department': 'Sales', 'Salary': '50000', 'JoinDate': '2018-05-12'}
# {'EmployeeID': '102', 'Name': 'Jane Smith', 'Department': 'Marketing', 'Salary': '55000', 'JoinDate': '2019-06-15'}
# {'EmployeeID': '103', 'Name': 'Emily Davis', 'Department': 'HR', 'Salary': '60000', 'JoinDate': '2017-09-23'}
# {'EmployeeID': '104', 'Name': 'Michael Brown', 'Department': 'Engineering', 'Salary': '75000', 'JoinDate': '2020-01-10'}
# {'EmployeeID': '105', 'Name': 'Linda Wilson', 'Department': 'Finance', 'Salary': '70000', 'JoinDate': '2016-11-20'}