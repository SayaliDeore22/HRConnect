"""
Write a program to get "HIRE DATE" of employee who's department is within range 30
to 110 AND who's salary is > 4200.
The output should be in following format.
{
"<HIRE DATE in YYYY-MM-DD format>": [
"<first_name last_name>",
...,
"<first_name last_name>"
],
}
Using csv library
"""

import csv
import datetime

getdata = {}
with open("employee.csv", "r") as fp:
    data = csv.DictReader(fp)

    for line in data:
        if 30 <= int(line["DEPARTMENT_ID"]) < 110 and int(line["SALARY"]) > 4200:
            date = datetime.datetime.strptime(line['HIRE_DATE'], "%d-%b-%y")
            fdate = date.strftime("%Y-%d-%m")
            if date in getdata:
                getdata[fdate].append(line["FIRST_NAME"] + " " + line["LAST_NAME"])
            else:
                getdata[fdate] = line["FIRST_NAME"] + " " + line["LAST_NAME"]

print(getdata)

