food = []
food_dict = { }
while True:
    try:
       food.append(input("").upper())
       if food[-1] in food_dict:
            food_dict[food[-1]] += 1
       else:
           food_dict[food[-1]] = 1
    except EOFError:
        #tri par ordre alphabétique manquant
        sorted_dict = {key: food_dict[key] for key in sorted(food_dict)}
        for keys,values in sorted_dict.items():
            print(values,keys)

        break
