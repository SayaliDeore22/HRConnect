import csv
class HandleCSV:
    filename = "E:\Velocity class\employee.csv"

    @classmethod
    def read_entire_csv(cls):
        data = []
        with open(cls.filename, "r") as fp:
            reader = csv.DictReader(fp)
            for line in reader:
                data.append(line)
        return data

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as bar:
            yield bar.readline()


if __name__ == "__main__":

    obj = HandleCSV()
    print(obj.read_entire_csv())
