import pandas as pd

df = pd.read_csv("population.csv")

southam_2000 = df[(df["continent"] == "South America") & (df["year"] == 2000)]

avg_population = southam_2000["population"].mean()
print(f"n\ Average population in South America in 2000: {avg_population}")

above_avg = southam_2000[southam_2000["population"] > avg_population]
below_avg = southam_2000[southam_2000["population"] < avg_population]

print("\n Countries above average:")
print(above_avg[["country name", "population"]])

print("\n Countries below average:")
print(below_avg[["country name", "population"]])