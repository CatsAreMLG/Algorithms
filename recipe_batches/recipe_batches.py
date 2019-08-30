#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    minIngredient = None
    for i in recipe:
        if i not in ingredients:
            return 0
        if not minIngredient or ingredients[i] / recipe[i] < minIngredient:
            minIngredient = ingredients[i] / recipe[i]
    return math.trunc(minIngredient)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5, 'cheese': 7}
    ingredients = {'milk': 132, 'butter': 51, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
