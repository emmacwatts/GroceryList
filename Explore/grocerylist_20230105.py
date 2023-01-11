#python code goes here
import pandas as pd
import random

#Import files
recipeIngredientsdf = pd.read_excel('~/GitHubProjects/GroceryList/InputFiles/RecipeIngredients.xlsx')
recipeInfodf = pd.read_excel('~/GitHubProjects/GroceryList/InputFiles/RecipeInfo.xlsx')
ingredientTags = pd.read_excel('~/GitHubProjects/GroceryList/InputFiles/IngredientTags.xlsx')

#Other parameters
numberOfLunches = 7
numberOfDinners = 7

# print(ingredientTags)

#Utils
#Take in user recipe specs
def userGrocerySpecs():
    dinnerVol, dinnersType = input("Enter the number of dinner recipes/portions desired. (e.g. 1 recipe or 5 portions) ").split()
    return dinnerVol, dinnersType

#Master df

#Define recipes

#Pick recipes
def defineLunchesandDinners():
    lunches = []
    dinners = []
    for recipe, type in zip(recipeInfodf["Recipe"], recipeInfodf["Meal Type"]):
        if "Lunch" in type:
            lunches.append(recipe)
        if "Dinner" in type:
            dinners.append(recipe)
    return lunches, dinners

def pickMeals():
    
#run.py
dinnerVol, dinnersType = userGrocerySpecs()
lunches, dinners = defineLunchesandDinners()