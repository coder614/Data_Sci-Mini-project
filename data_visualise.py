import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("My_1W_screen_time.csv")

Days = data["Days"]
YT = data["YT"]
Insta = data["Insta"]
Inshort = data["Inshort"]
WhatsApp = data["WhatsApp"]
BGMI = data["BGMI"]

# stack plot chart data
labels = ['YT', 'Insta', 'Inshort', 'WhatsApp', 'BGMI']
plt.stackplot(Days, YT, Insta, Inshort, WhatsApp, BGMI, labels=labels)
plt.legend(loc="upper left")
plt.grid(True)
plt.title("My 1 weak mobile screen time")
plt.ylabel("Hours")
plt.xlabel("Weak Days")
plt.xticks(Days, ["Mon", "Tues", "Weds", "Thurs", "Fri", "Sat", "Sun"])
plt.show()