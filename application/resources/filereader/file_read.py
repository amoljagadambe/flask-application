import os
import csv

path = os.path.abspath(os.path.dirname(__name__))
print(path)

file = open(path + "/files/total-words.txt", "r")
out_file = open(path + "/files/output.csv", "w")
for line in file:
    out = line.split(' ')
    print(out)
    writer = csv.writer(out_file, delimiter=',')
    writer.writerows(out)
