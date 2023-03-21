import json
import pandas as pd
from IPython.display import display

json_data = json.load(open("../analysis/sorted_data.json"))
print(json_data)