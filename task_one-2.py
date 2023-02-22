"""

Write a program to get details of employees who's salary is > 9000. The output should
be in following format
{
"Name": "<first_name last_name>",
"email": "<email>",
"phone number": "<phone number without DOT>"
}
Using csv library

"""

import csv

EmployeeData = []
with open("employee.csv", "r") as fp:
    reader = csv.DictReader(fp)

    for line in reader:
        if int(line['SALARY']) > 3000:
            phonenumber = line['PHONE_NUMBER'].split('.')
            phonenumber = "".join(phonenumber)

            EmployeeData.append({"Name": line['FIRST_NAME'] + "" + line['LAST_NAME'], "EMAILS": line['EMAIL'],
                                 "phone number": phonenumber})

print(EmployeeData)
