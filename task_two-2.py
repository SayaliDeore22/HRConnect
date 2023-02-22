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
Using function
"""

from datetime import datetime
from my_utils.csv_file import HandleCSV


def get_details():
    reader = HandleCSV.read_entire_csv()
    getdata = {}

    for line in reader:
        if 30 <= int(line["DEPARTMENT_ID"]) < 110 and  int(line["SALARY"]) > 4200:
            date = datetime.strptime(line['HIRE_DATE'], "%d-%b-%y")
            fdate = date.strftime("%Y-%d-%m")
            if date in getdata:
                getdata[fdate].append(line["FIRST_NAME"] + " " + line["LAST_NAME"])
            else:
                getdata[fdate] = line["FIRST_NAME"] + " " + line["LAST_NAME"]

    return getdata


if __name__ == "__main__":
    print((get_details()))