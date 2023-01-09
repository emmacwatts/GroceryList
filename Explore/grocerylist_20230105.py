#python code goes here
import pandas as pd
import openpyxl

#Import files
recipeIngredientsdf = pd.read_excel('/home/user/Documents/GitHub/GroceryList/GroceryList/InputFiles/RecipeIngredients.xlsx')
recipeInfodf = pd.read_excel('/home/user/Documents/GitHub/GroceryList/GroceryList/InputFiles/RecipeInfo.xlsx')
ingredientTags = pd.read_excel('/home/user/Documents/GitHub/GroceryList/GroceryList/InputFiles/IngredientTags.xlsx')

#Other parameters
numberOfLunches = 7
numberOfDinners = 7

print(ingredientTags)

#Take in user recipe specs
def userGrocerySpecs():
    input()

#Master df
