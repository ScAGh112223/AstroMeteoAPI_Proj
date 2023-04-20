from itertools import chain
import requests
import geopy
from matplotlib import pyplot as plt
import numpy as np

address = "9111 116"

locator = geopy.Nominatim(user_agent="myGeocoder")
# locator.geocode({"street":address, 'state': "british columbia", "country": "canada"})
# print(locator.geocode(address).latitude)c

# loc = locator.geocode(query={"street":'501 Belleville', 'city': 'victoria', 'postcode': 'V8V 2L8' , 'state': "british columbia", "country": "canada"})

res = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude=49.169335&longitude=-122.901486&current_weather=false&hourly=cloudcover,cloudcover_low,cloudcover_mid,cloudcover_high,dewpoint_2m")

forecast = res.json()

hours = [t[-5:-3] for t in forecast["hourly"]["time"]]

_, axes = plt.subplots(nrows=2, ncols=3)
_, axes2 = plt.subplots(nrows=2, ncols=3)

print(hours)

x = np.zeros(len(forecast["hourly"]["time"]))

si = 0
for axis in list(chain.from_iterable(zip(*axes2))):
    sn = si+23
    axis.plot(hours[si:sn], forecast['hourly']['cloudcover_high'][si:sn], color="g")
    axis.plot(hours[si:sn], forecast['hourly']['cloudcover_mid'][si:sn], color="y")
    axis.plot(hours[si:sn], forecast['hourly']['cloudcover_low'][si:sn], color="r")
    axis.plot(hours[si:sn], forecast['hourly']['cloudcover'][si:sn], color="b")
    si = sn

# axes[0,0].plot(hours[:22], forecast['hourly']['cloudcover'][:22])
# axes[0,0].plot(hours[:22], forecast['hourly']['cloudcover_low'][:22])
# axes[0,0].plot(hours[:22], forecast['hourly']['cloudcover_mid'][:22])
# axes[0,0].plot(hours[:22], forecast['hourly']['cloudcover_high'][:22])

# axes[0,1].plot(hours[22:44], forecast['hourly']['cloudcover'][22:44])
# axes[0,1].plot(hours[22:44], forecast['hourly']['cloudcover_low'][22:44])
# axes[0,1].plot(hours[22:44], forecast['hourly']['cloudcover_mid'][22:44])
# axes[0,1].plot(hours[22:44], forecast['hourly']['cloudcover_high'][22:44])

# axes[0,2].plot(hours[44:66], forecast['hourly']['cloudcover'][44:66])
# axes[0,2].plot(hours[44:66], forecast['hourly']['cloudcover_low'][44:66])
# axes[0,2].plot(hours[44:66], forecast['hourly']['cloudcover_mid'][44:66])
# axes[0,2].plot(hours[44:66], forecast['hourly']['cloudcover_high'][44:66])

# axes[1,0].plot(hours[66:88], forecast['hourly']['cloudcover'][66:88])
# axes[1,0].plot(hours[66:88], forecast['hourly']['cloudcover_low'][66:88])
# axes[1,0].plot(hours[66:88], forecast['hourly']['cloudcover_mid'][66:88])
# axes[1,0].plot(hours[66:88], forecast['hourly']['cloudcover_high'][66:88])

# axes[1,1].plot(hours[88:100], forecast['hourly']['cloudcover'][88:100])
# axes[1,1].plot(hours[88:100], forecast['hourly']['cloudcover_low'][88:100])
# axes[1,1].plot(hours[88:100], forecast['hourly']['cloudcover_mid'][88:100])
# axes[1,1].plot(hours[88:100], forecast['hourly']['cloudcover_high'][88:100])

# axes[1,2].plot(hours[100:122], forecast['hourly']['cloudcover'][100:122])
# axes[1,2].plot(hours[100:122], forecast['hourly']['cloudcover_low'][100:122])
# axes[1,2].plot(hours[100:122], forecast['hourly']['cloudcover_mid'][100:122])
# axes[1,2].plot(hours[100:122], forecast['hourly']['cloudcover_high'][100:122])

# plt.plot(hours[122:144], forecast['hourly']['cloudcover'][122:144])

for i, t in enumerate(forecast["hourly"]["time"]):
    print(f"Time: {t}, forecast: {forecast['hourly']['cloudcover'][i]}")

plt.show()
print(res.json())