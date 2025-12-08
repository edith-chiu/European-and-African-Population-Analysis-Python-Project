import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("population.csv")

print(df.head())

africa_2010 = df[(df["continent"] == "Africa") & (df["year"] == 2010)]

total_africa_2010 = africa_2010["population"].sum()
print(f"\n Total population in Africa 2010: {total_africa_2010}")

plt.figure(figsize=(12,6))
plt.bar(africa_2010["country name"], africa_2010["population"])
plt.title("Population distribution across African countries in 2010")
plt.xlabel("Country")
plt.ylabel("Population")
plt.show()