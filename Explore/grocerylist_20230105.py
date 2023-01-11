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
def defineLunchesandDinners(recipeInfodf):
    lunches = []
    dinners = []
    for recipe, type in zip(recipeInfodf["Recipe"], recipeInfodf["Meal Type"]):
        if "Lunch" in type:
            lunches.append(recipe)
        if "Dinner" in type:
            dinners.append(recipe)
    return lunches, dinners

def pickMeals(lunches, dinners, recipeInfodf, dinnerVol, dinnersType):
    selectedDinners = []
    firstSelectedDinner = random.choice(dinners)
    selectedDinners.append(firstSelectedDinner)
    selectedDinnerPortions = int(recipeInfodf.loc[recipeInfodf["Recipe"] == firstSelectedDinner, "Serves"])
    # if selectedDinnerPortions < int(dinnerVol):
    #     remainingPortions = int(dinnerVol)-selectedDinnerPortions
    #     if remainingPortions < max(recipeInfodf["Serves"]):
    #         remainingPortionRecipes = recipeInfodf[recipeInfodf["Serves"] == remainingPortions]
    #         nextSelectedDinner = random.choice(remainingPortionRecipes)
    #         selectedDinners.append(nextSelectedDinner)
    #         selectedDinnerPortions += int(recipeInfodf.loc[recipeInfodf["Recipe"] == nextSelectedDinner, "Serves"])

    return selectedDinners

def printIngredients(recipeIngredientsdf, pickedMeals):
    groceryList = []
    for meal in pickedMeals:
        mealIngredientsdf = recipeIngredientsdf[recipeIngredientsdf["Recipe"] == meal]
        for index, row in mealIngredientsdf.iterrows():
            ingredientsAndQuantity = str(row["Ingredients"]) + " " + str(row["Quantity"]) + " " + str(row["Unit"])
            groceryList.append(ingredientsAndQuantity)

    return groceryList

#run.py
dinnerVol, dinnersType = userGrocerySpecs()
lunches, dinners = defineLunchesandDinners(recipeInfodf)
pickedMeals = pickMeals(lunches, dinners, recipeInfodf, dinnerVol, dinnersType)
groceryList = printIngredients(recipeIngredientsdf, pickedMeals)

print(groceryList)