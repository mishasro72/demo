# Var 1
# def cakes(recipe, available):
#     count = []
#     for key, value in recipe.items():
#         if available[key]:
#             count.append(available[key] // value)
#         else:
#             return False
#     return False if 0 in count else min(count)

# Var 2 
def cakes(recipe, available):
    return min(available.get(key, 0)// recipe[key] for key in recipe)

print(cakes({'flour' : 500, 'sugar' : 200, 'eggs' : 1}, {'flour' : 1200, 'sugar' : 1200, 'eggs' : 5, 'milk' : 200}))
recept = {'flour' : 500, 'sugar' : 200, 'eggs' : 1}
# for key, value in recept.items():
#     print (key, value)
# for i in recept:
#      print(i)
#1
