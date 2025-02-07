import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("timeseries.csv", sep=";")
df = df.loc[:, ["Date", "A"]]
df = df.sort_values(by="Date")
plt.plot(df["Date"], df["A"], marker="o", linestyle="-", color="b", label="Value")
plt.show()
