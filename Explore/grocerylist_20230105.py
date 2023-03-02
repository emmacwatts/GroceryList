import pandas as pd
import random

#Import files
recipeIngredientsdf = pd.read_excel('~/GitHubProjects/GroceryList/InputFiles/RecipeIngredients.xlsx')
recipeInfodf = pd.read_excel('~/GitHubProjects/GroceryList/InputFiles/RecipeInfo.xlsx')
ingredientTags = pd.read_excel('~/GitHubProjects/GroceryList/InputFiles/IngredientTags.xlsx')

#Other parameters
numberOfLunches = 7
numberOfDinners = 7

#run.py
dinnerVol, dinnersType = userGrocerySpecs()
lunches, dinners = defineLunchesandDinners(recipeInfodf)
pickedMeals = pickMeals(lunches, dinners, recipeInfodf, dinnerVol, dinnersType)
groceryList = printIngredients(recipeIngredientsdf, pickedMeals)

print(groceryList)