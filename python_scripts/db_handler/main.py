import csv 

with open("people.csv") as fin, open ("filtered.csv", "w", newline="") as fout:
    reader = csv.DictReader(fin)
    writer = csv.DictWriter(fout, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        if int(row["age"]) > 25:
            writer.writerow(row)