# import libraries
import pandas as pd

# Get the dataset to work with
dataFrame = pd.read_csv("cleaned_and_parsed_dataset.csv")
print(dataFrame)
#genres I need
desired_values = ["alt-rock", "alternative","black-metal", "death-metal", "emo", "funk", "garage", "goth", "grindcore", "groove", "grunge", "hard-rock", "heavy-metal", "industrial", "j-rock", "metal", "metalcore", "psych-rock", "punk", "punk-rock", "rock", "rock-n-roll"]

dataFrame = dataFrame[dataFrame['track_genre'].isin(desired_values)]

# print dataFrame info
print("Cleaned Data Info:")
print(dataFrame)

dataFrame.to_csv("cleaned_and_parsed_dataset.csv", sep=',', index=False, encoding='utf-8')