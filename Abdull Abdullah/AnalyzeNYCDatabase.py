import csv

f = open("Analyze NYC Database.py","r+")
csv_f = csv.reader(f)
for row in csv_f:
        print(row)
f.close()

with open("Analyze NYC Database.py","r+") as f:
        reader = csv.reader(f)
        for row in reader:
                print(row)
        f.close()

with open("Analyze NYC Database.py","r+") as f:
        writer = csv. writer(f)
        writer.writerow(["John","Greg","Bill"])
        f.close()

input()
