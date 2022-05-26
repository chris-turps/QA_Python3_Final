class Drink:
    def __init__(self
        , drink_name
        , water_ml
        , beans_g
        , milk_ml
        , cost_p
    ):
        self.name = drink_name
        self.water = water_ml
        self.beans = beans_g
        self.milk = milk_ml
        self.cost = cost_p

# americano_obj = Drink("americano",150,10,0,249)
# latte_obj = Drink("latte",100,10,50,279)
# cappuccino_obj = Drink("cappuccino",75,10,75,299)
# espresso_obj = Drink("espresso",50,10,0,219)
# 
# drinkList = [americano_obj,latte_obj,cappuccino_obj,espresso_obj]
# drinkTypes = [drink.name for drink in drinkList]