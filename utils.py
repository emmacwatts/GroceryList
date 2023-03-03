def defineIngredientTags():
    """
    Define unique ingredients in the RecipeIngredients list and prompt user to input tags.
    """
    import pandas as pd
    recipeIngredientsdf = pd.read_excel('InputFiles/RecipeIngredients.xlsx')
    ingredients = set(recipeIngredientsdf["Ingredients"])
    ingredientsTags = pd.DataFrame(data = ingredients, columns= ["Ingredients"])
    ingredientsTags["Tags"] = ""
    for ind,row in ingredientsTags.iterrows():
        row["Tags"] = input(f"Enter the tags for the ingredient {row['Ingredients']}.")
    ingredientsTags.to_excel("InputFiles/IngredientTags.xlsx", index = False)

def userGrocerySpecs():
    """
    Take in user recipe specs.
    """
    desiredPortions = {}
    desiredPortions['Breakfast'], desiredPortions['Lunch'], desiredPortions['Dinner'], desiredPortions['Bars'], desiredPortions['Fruit'], desiredPortions['Savoury Snack'], desiredPortions['Baking'] = input("Enter the number of breakfast, lunch, and dinner portions desired. Then enter portions of bars, fruits, savoury snacks, and baking items. ").split()
    
    for item in desiredPortions.keys():
        desiredPortions[item] = int(desiredPortions[item])
        
    return desiredPortions

def all_sums(input_list):
    """
    Made by chatGPT.
    This function takes a list of integers as input, and returns a set of all possible sums that can be formed
    using the elements of the list.
    """
    result_set = set()
    n = len(input_list)
    for i in range(1, 2**n):
        binary_string = format(i, '0' + str(n) + 'b')
        sum_val = 0
        for j in range(n):
            if binary_string[j] == '1':
                sum_val += input_list[j]
        result_set.add(sum_val)
    return result_set

def defineMealTypes():
    """
    Define lists for food types.
    """
    import pandas as pd
    
    recipeInfodf = pd.read_excel('InputFiles/RecipeInfo.xlsx')

    mealTypeRecipes = {'Lunch': [], 'Dinner' : [], 'Breakfast' : [], "Bars" : [], "Fruit" : [], "Savoury Snack" : [], "Baking" : []}
    mealTypePortions = {'Lunch': [], 'Dinner' : [], 'Breakfast' : [], "Bars" : [], "Fruit" : [], "Savoury Snack" : [], "Baking" : []}

    for recipe, type in zip(recipeInfodf["Recipe"], recipeInfodf["Meal Type"]):
        for key in mealTypeRecipes.keys():
            if key in type:
                mealTypeRecipes[key].append(recipe)
    
    for type, portions in zip(recipeInfodf["Meal Type"], recipeInfodf["Serves"]):
        for key in mealTypePortions.keys():
            if key in type:
                mealTypePortions[key].append(portions)
    
    #possible portions will now represent all possible sums for that mealtype
    possiblePortions = {}
    for meal in mealTypePortions:
        possiblePortions[meal] = all_sums(mealTypePortions[meal])
    
    return mealTypeRecipes, mealTypePortions, possiblePortions

def pickMeals(desiredPortions, mealTypeRecipes, mealTypePortions, possiblePortions):
    """
    Selects meals for the required portions for each type.
    """
    import random

    selectedMeals = {}

    for type in mealTypeRecipes.keys():
        portions = desiredPortions[type]
    
        #check that it's possible to get this number of portions
        while portions not in possiblePortions[type]:
            print(f"Not possible to get this number of portions for {type} given these recipes. Adding one portion.")
            portions += 1
            break

        possibleMeals = []
        for ind, mealPortion in enumerate(mealTypePortions[type]):
            if mealPortion == portions:
                possibleMeals.append(mealTypeRecipes[type][ind])
        
        if possibleMeals == []:
            print(f"Not possible to get this number of meals for {type}.")
        else:
            selectedMeals[type] = random.choice(possibleMeals)

    return selectedMeals

def getIngredientsListbySection(selectedMeals):

    """
    Prints ingredients list of the selected meals by section of the grocery store.

    """

    import pandas as pd
    import numpy as np

    recipeIngredientsdf = pd.read_excel("InputFiles/RecipeIngredients.xlsx")
    IngredientsTags = pd.read_excel("InputFiles/IngredientTags.xlsx")

    ingredientsAndTags = pd.merge(recipeIngredientsdf, IngredientsTags, on='Ingredients', how='inner')

    desiredRecipes = list(selectedMeals.values())
    selectedRecipes = ingredientsAndTags.loc[ingredientsAndTags["Recipe"].isin(desiredRecipes)]
    
    selectedRecipes = selectedRecipes[["Tags", 'Ingredients', "Quantity", "Unit", "Recipe"]]
    selectedRecipes = selectedRecipes.set_index("Tags", drop = True)
    selectedRecipes = selectedRecipes.sort_index()
    selectedRecipes = selectedRecipes.replace(np.nan, "")

    return selectedRecipes

def makeGroceryList(outputFile):
    """
    Makes a grocery list organised by ingredient type for the specified portion of recipes per meal type, defined by the user.

    """

    desiredPortions = userGrocerySpecs()

    mealTypeRecipes, mealTypePortions, possiblePortions = defineMealTypes()

    selectedMeals = pickMeals(desiredPortions, mealTypeRecipes, mealTypePortions, possiblePortions)

    selectedRecipes = getIngredientsListbySection(selectedMeals)

    selectedRecipes.to_excel("outputFiles/groceryList.xlsx")

    return selectedRecipes