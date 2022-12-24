import json_lines
from sys import argv

v1 = []
v2 = []
v3 = ""

with open("list.jl", "rb") as f:
 for item in json_lines.reader(f):
  v1.append(item["text"])
  v2.append(item["href"])

fh = open(argv[1], "w")
for i in v2: fh.write(i[0] + "\n")
fh.close()
