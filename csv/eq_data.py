import json
import matplotlib.pyplot as plt


file_name="data/eq_data/eq_data_1_day_m1.json"
with open(file_name) as f:
    load_data=json.load(f)
file_name2="data/readable_eq_data.json"
with open(file_name2,'w') as f:
    json.dump(load_data, f, indent=4)





