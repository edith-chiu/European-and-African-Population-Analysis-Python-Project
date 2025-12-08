import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("population.csv")

europe2000 = df[(df["continent"] == "Europe") & (df["year"] == 2000)]
europe2010 = df[(df["continent"] == "Europe") & (df["year"] == 2010)]

europe_growth = pd.merge(europe2000, europe2010, on="country name", suffixes =("2000", "2010"))
europe_growth["growth"] = europe_growth["population2010"] - europe_growth["population2000"]

total_growth_europe = europe_growth["growth"].sum()
print(f"\n Total population growth in Europe (2000-2010): {total_growth_europe}")

top5_growth = europe_growth.nlargest(5, "growth")
print("\n Top 5 European countries by population growth:")
print(top5_growth[["country name", "growth"]])

plt.figure(figsize=(10,6))
for country in top5_growth["country name"]:
    country_data = df[(df["country name"] == country) &
                      (df["continent"] == "Europe") &
                      (df["year"].between(2000, 2010))]
    plt.plot(country_data["year"], country_data["population"],label=country)

plt.title("Population growth in Top 5 European Countries (2000-2010)")
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend()
plt.show()