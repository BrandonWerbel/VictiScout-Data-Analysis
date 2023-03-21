from try_parse.utils import ParseUtils
import json

def parse(str):
    if ParseUtils.try_parse_int(str)[0]:
        return int(str)
    elif ParseUtils.try_parse_bool(str)[0]:
        return ParseUtils.try_parse_bool(str)[1]
    else:
        return str

# get data from csv file
data_lines = open("../analysis/scouting-data.csv", "r").readlines()
header = data_lines[0]
tail = [d.strip() for d in data_lines[1:]]

# split into header and "tail" (data array)
header = header.split(",")
tail = [d.split(",", len(header)-1) for d in tail]

# parse and sort data
tail = [[parse(i) for i in line] for line in tail]
tail.sort(key=lambda d: d[0])

# convert data to JSON
team = -1
data = {header[0]: [header[1:]]}
for l in tail:
    if l[0] != team:
        data[str(l[0])] = []
        team = l[0]
    data[str(l[0])].append(l[1:])

# write JSON to file
sorted_data = open("../analysis/sorted_data.json", "w")
sorted_data.write(json.dumps(data))
sorted_data.close()