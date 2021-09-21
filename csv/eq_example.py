import json
import matplotlib.pyplot as plt

fig,ax = plt.subplots()
file_name="data/eq_data/eq_data_1_day_m1.json"
with open(file_name) as f:
    load_data=json.load(f)

all_eq_dicts= load_data["features"]
# print(len(all_eq_dicts))
result=[]
lon=[]
lat=[]
for i in all_eq_dicts:
    meg= i['properties']["mag"]
    lan=i["geometry"]["coordinates"][0]
    long=i["geometry"]["coordinates"][1]
    result.append(meg)
    lon.append(lan)
    lat.append(long)

# ax.scatter(result,lon,c="red",s=10)
print(lon[0:10])
print(lat[0:10])
print(result[0:10])
# plt.show()

