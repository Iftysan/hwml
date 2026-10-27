
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
matches = pd.read_csv("titanic.csv", sep="\t")

matches = matches.drop(columns=["Cabin"])
matches = matches.dropna()

print(matches.head())
print(matches.isnull().sum())

sns.countplot(data=matches, x="Survived")
plt.title("Survived People and Dead People")

plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of People")

plt.show()

sns.countplot(data=matches, x="Survived", hue="Sex")
plt.title("Survived People: Male and Female")

plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of People")

plt.show()

sns.countplot(data=matches, x="Sex", hue="Survived")
plt.title("Number of Male and Female Survivors")

plt.xlabel("Gender")
plt.ylabel("Number of People")

plt.show()

sns.countplot(data=matches, x="Pclass", hue="Survived")
plt.title("Survived People and Passenger Class")

plt.xlabel("Passenger Class")
plt.ylabel("Number of People")

plt.show()