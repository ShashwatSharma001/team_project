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


# 3rd graph, most common genres.

# count the most common genres
genres = df["listed_in"].dropna().str.split(",").explode().str.strip()

top_genres = genres.value_counts().head(10)

# 3rd graph building
top_genres.sort_values().plot(kind="barh", color="purple")

plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")

plt.tight_layout()
plt.savefig("graphs/top_10_genres.png")
plt.show()
plt.close()

# 4th graph most featured actors
# count actor appearances
actors = df["cast"].dropna().str.split(",").explode().str.strip()

top_actors = actors.value_counts().head(10)

top_actors.sort_values().plot(kind="barh", color="green")

plt.title("Top 10 Most Featured Netflix Actors")
plt.xlabel("Number of Titles")
plt.ylabel("Actor")

plt.tight_layout()
plt.savefig("graphs/top_10_actors.png")
plt.show()
plt.close()


# 5th graph, average movie duration by year
# count actor appearances
actors = df["cast"].dropna().str.split(",").explode().str.strip()

top_actors = actors.value_counts().head(10)

top_actors.sort_values().plot(kind="barh", color="green")

plt.title("Top 10 Most Featured Netflix Actors")
plt.xlabel("Number of Titles")
plt.ylabel("Actor")

plt.tight_layout()
plt.savefig("graphs/top_10_actors.png")
plt.show()
plt.close()
