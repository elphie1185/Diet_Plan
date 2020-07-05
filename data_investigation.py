# import libraries
import pandas as pd

# improve outplut display
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

# look at the data sets
cal_per_exercise_data = pd.read_csv("Data/calorie_burn_per_exercise.csv")
print(cal_per_exercise_data.head(20))
print(cal_per_exercise_data.columns)
print(cal_per_exercise_data.info())
print(cal_per_exercise_data.describe())

mood_data = pd.read_csv("Data/food_exercise_effect_on_mood.csv")
print(mood_data.head(20))
print(mood_data.columns)
print(mood_data.info())
print(mood_data.describe())

recipe_data = pd.read_csv("Data/recipe_data.csv")
print(recipe_data.head(20))
print(recipe_data.columns)
print(recipe_data.info())
print(recipe_data.describe())