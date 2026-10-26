import pandas as pd
import matplotlib.pyplot as plt

# read the dataset
df = pd.read_csv("data/netflix_titles.csv")

# count movies and tv shows
movies = df["type"].value_counts()

print(movies)

# first graph
movies.plot(kind="bar", color=["red", "blue"])

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Number of Titles")
plt.xticks(rotation=0)

plt.savefig("graphs/movies_vs_tvshows.png")
plt.show()
plt.close()

# convert dates
df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), errors="coerce")
df["year_added"] = df["date_added"].dt.year

# count titles by year
years = df.groupby(["year_added", "type"]).size().unstack(fill_value=0)

print(years)

# second graph
years.plot(kind="line", marker="o")

plt.title("Netflix Content Added Over Time")
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")

plt.savefig("graphs/netflix_content_over_time.png")
plt.show()
plt.close()