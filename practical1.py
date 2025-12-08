import pandas as pd

df = pd.read_csv("population.csv")

no_population_2000 = df[(df["year"] == 2000) & (df["population"] == 0)]

countries_no_population_2000 = no_population_2000[["country name", "continent"]].drop_duplicates()

count = countries_no_population_2000.shape[0]
print(f"Number of countries with no pop data in 2000: {count}")

print(countries_no_population_2000)