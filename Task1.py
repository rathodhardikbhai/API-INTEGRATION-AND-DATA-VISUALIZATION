import requests
import pandas as pd

# Fetch data from JSONPlaceholder API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Convert JSON to Python list/dict
    # print("Data fetched successfully!")
else:
    print(f"Error: {response.status_code}")

df = pd.DataFrame(data)
# print(df.head())  # Show first 5 rows

#First Chart Data
import matplotlib.pyplot as plt

# Count posts per user
posts_per_user = df['userId'].value_counts().sort_index()

# Plot
plt.figure(figsize=(10, 5))
posts_per_user.plot(kind='bar', color='skyblue')
plt.title("Number of Posts per User")
plt.xlabel("User ID")
plt.ylabel("Post Count")
plt.grid(axis='y')
plt.show()



#Second Chart Data
from wordcloud import WordCloud

# Combine all titles into a single string
text = " ".join(df['title'].astype(str))

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Most Frequent Words in Post Titles")
plt.show()

# # Fetch COVID-19 data
# import seaborn as sns
# url = "https://disease.sh/v3/covid-19/all"
# response = requests.get(url)
# covid_data = response.json()

# # Convert to DataFrame
# covid_df = pd.DataFrame({
#     "Metric": ["Cases", "Deaths", "Recovered", "Active"],
#     "Count": [
#         covid_data["cases"],
#         covid_data["deaths"],
#         covid_data["recovered"],
#         covid_data["active"]
#     ]
# })

# # Plot
# plt.figure(figsize=(8, 5))
# sns.barplot(x="Metric", y="Count", data=covid_df, palette="viridis")
# plt.title("Global COVID-19 Statistics")
# plt.show()