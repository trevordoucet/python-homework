import os
import csv

cereal_csv = os.path.join("../Resources", "cereal.csv")
with open(cereal_csv, 'r') as file:
    csv_reader=csv.reader(file)
    next(csv_reader, None)
    for row in csv_reader:
        fiberCount = row[8]
        if float (fiberCount) >= 5:
            lines = file.read()
            print(lines)