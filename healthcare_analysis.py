import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("DoctorVisits.csv")

print("\n=== DATASET INFO ===")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nGender counts:")
print(df["gender"].value_counts())

print("\n=== INCOME ===")
print("Minimum:", df["income"].min())
print("Maximum:", df["income"].max())
print("Mean:", df["income"].mean())

print("\n=== REDUCED ACTIVITY BY GENDER (MEAN) ===")
print(df.groupby("gender")["reduced"].mean())

print("\n=== PEOPLE BY ILLNESS COUNT ===")
print(df["illness"].value_counts().sort_index())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== INCOME / VISITS CORRELATION ===")
print(df[["income", "visits"]].corr().loc["income", "visits"])

print("\n=== TOTAL ILLNESS COUNT BY GENDER ===")
print(df.groupby("gender")["illness"].sum())

print("\n=== INSURANCE INDICATORS (%) ===")
for col in ["private", "freepoor", "freerepat"]:
    pct = df[col].astype(str).str.lower().eq("yes").mean() * 100
    print(col, round(pct, 2))

print("\n=== TOTAL REDUCED DAYS BY GENDER ===")
print(df.groupby("gender")["reduced"].sum())

# Visualizations
sns.set_theme(style="whitegrid")

plt.figure(figsize=(8,5))
sns.countplot(data=df, x="gender")
plt.title("Number of Male and Female Patients")
plt.show()

illness_counts = df["illness"].value_counts().sort_index()
plt.figure(figsize=(8,5))
sns.barplot(x=illness_counts.index.astype(str), y=illness_counts.values)
plt.title("Number of People by Illness Count")
plt.xlabel("Number of Illnesses")
plt.ylabel("Number of People")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="income", y="visits", alpha=.45)
plt.title("Income vs Number of Hospital Visits")
plt.show()

reduced = df.groupby("gender")["reduced"].sum().sort_values()
plt.figure(figsize=(8,5))
reduced.plot(kind="barh")
plt.title("Total Reduced-Activity Days Due to Illness by Gender")
plt.xlabel("Reduced Days")
plt.show()

sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.show()
