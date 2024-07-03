import csv


def readCSVFile(file_path):
    data_list = []
    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)
        for line in reader:
            data_list.append(line)
    return data_list

