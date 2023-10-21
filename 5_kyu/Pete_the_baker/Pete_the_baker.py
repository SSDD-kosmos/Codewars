def cakes(recipe, available):
    res = []
    list_keys = list(recipe.keys())
    if len(recipe) > len(available):
        return 0
    for i in range(len(list_keys)):
        if list_keys[i] in available:
            res.append(available.get(list_keys[i]) // recipe.get(list_keys[i]))
        else:
            return 0
    return min(res)

# def cakes(recipe, available):
#     return min([available[i]//recipe[i] if i in recipe else 0 for i in recipe])


cakes({"flour": 500, "sugar": 200, "eggs": 1},
      {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
