CHEESES=["cheddar", "gouda", "camembert"]

def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        print(str(dwarves.index(dwarf)+1) + '. ' + dwarf)

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + '!' for call in planeteer_calls]
    

def long_planeteer_calls(calls):
    x= any(len(call) > 4 for call in calls)
    return x

def find_the_cheese(foods):
    x =next((food for food in foods if food in CHEESES), None)
    return x

    # for food in foods:
    #     if food in CHEESES:
    #         return food
    # return None
