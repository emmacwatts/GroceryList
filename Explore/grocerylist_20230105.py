#python code goes here
import pandas as pd

#Import files
recipeIngredientsdf = pd.read_excel('/Users/ecwatts/Desktop/Uni/Oxford DTP/GitHub Projects/GroceryList/InputFiles/RecipeIngredients.xlsx')
recipeInfodf = pd.read_excel('/home/user/Documents/GitHub/GroceryList/GroceryList/InputFiles/RecipeInfo.xlsx')
ingredientTags = pd.read_excel('/home/user/Documents/GitHub/GroceryList/GroceryList/InputFiles/IngredientTags.xlsx')

#Other parameters
numberOfLunches = 7
numberOfDinners = 7

print(ingredientTags)

#Take in user recipe specs
def userGrocerySpecs():
    dinnerVol, dinnersType = input("Enter the number of dinner recipes/portions desired. (e.g. 1 recipe or 5 portions)")

#Master df

#Define recipes