import csv


def csv_to_json_data_migration(filename):
    with open(filename, encoding="cp1251") as f:
        file_data = csv.reader(f)
        headers = next(file_data)
        return [dict(zip(headers, i)) for i in file_data]
