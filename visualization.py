import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("quotes.csv")
print(df.head())
df["length"] = df["Quotes"].apply(len)
plt.figure()
plt.hist(df["length"])
plt.title("Distribution of Quote Lengths")
plt.xlabel("Length of Quotes")
plt.ylabel("Frequency")
plt.show()
short = (df["length"] < 50).sum()
medium = ((df["length"] >= 50) & (df["length"] < 100)).sum()
long = (df["length"] >= 100).sum()

categories = ["Short", "Medium", "Long"]
values = [short, medium, long]

plt.figure()
plt.bar(categories, values)
plt.title("Quote Length Categories")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()
plt.figure()
plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.title("Quote Length Distribution (Percentage)")
plt.show()
plt.figure()
plt.scatter(range(len(df)), df["length"])
plt.title("Quote Length Spread")
plt.xlabel("Index")
plt.ylabel("Length")
plt.show()