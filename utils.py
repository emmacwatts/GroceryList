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
    desiredPortions['Breakfast'], desiredPortions['Lunches'], desiredPortions['Dinners'], desiredPortions['Bars'], desiredPortions['Fruit'], desiredPortions['Savoury Snack'], desiredPortions['Baking'] = input("Enter the number of breakfast, lunch, and dinner portions desired. Then enter portions of bars, fruits, savoury snacks, and baking items. ").split()

    return desiredPortions

def defineMealTypes(recipeInfodf):
    """
    Define lists for food types.
    """
    mealTypeRecipes = {'Lunch': [], 'Dinner' : [], 'Breakfast' : [], "Bars" : [], "Fruit" : [], "Savoury Snack" : [], "Baking" : []}

    for recipe, type in zip(recipeInfodf["Recipe"], recipeInfodf["Meal Type"]):
        for key in mealTypeRecipes.keys():
            if key in type:
                mealTypeRecipes[key].append(recipe)
            
    return mealTypeRecipes

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