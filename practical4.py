import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("population.csv")

world_2007 = df[df["year"] == 2007]
over1000m = world_2007[world_2007["population"] > 1000]

print("\n Countries with population > 1000million in 2007:")
print(over1000m[["country name", "population"]])

plt.figure(figsize=(10,6))
plt.scatter(world_2007["country name"], world_2007["population"], label="All countries")
plt.scatter(over1000m["country name"], over1000m["population"], color = 'red', label = ">1000m")
plt.xlabel("Country")
plt.ylabel("Population (millions)")
plt.title("Country population in 2007 > 1000m")
plt.legend()
plt.show()