"""

Write a program to get details of employees who's salary is > 9000. The output should
be in following format
{
"Name": "<first_name last_name>",
"email": "<email>",
"phone number": "<phone number without DOT>"
}
Using function

"""

from my_utils.csv_file import HandleCSV


def get_details():
    reader = HandleCSV.read_entire_csv()
    getdata = []
    for data in reader:
        if int(data["SALARY"]) > 9000:
            getdata.append({"Name":data["FIRST_NAME"]+" "+data["LAST_NAME"], "Email":data["EMAIL"],
            "Phone number":data["PHONE_NUMBER"].replace(".", "")})

    return getdata


if __name__ == "__main__":
    print(get_details())
