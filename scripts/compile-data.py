import os

path = "../scouting-data-files"

# open all csv files from VictiScout
files = [open(path + "/" + f) for f in os.listdir(path)]

# create new file for compiled data
if not os.path.exists("../analysis"):
    os.mkdir("../analysis")
compiled_data = open("../analysis/scouting-data.csv", "w")

# skip header in csv for all but the first file
for f in files[1:]:
    next(f)

# write VictiScout files to compiled data file
for f in files:
    compiled_data.write(f.read() + "\n")
