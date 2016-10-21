from enum import Enum


class FoodType(Enum):
    appetizer = 1
    main_course = 2
    garnish = 3
    desert = 4

# name, type, priority
prefered_food = [
    ("окрошка с курицей", FoodType.appetizer, 1),
    ("cуп пюре из цукини", FoodType.appetizer, 1.4),
    ("cуп гороховый", FoodType.appetizer, 1.2),
    ("пюре картофельное", FoodType.main_course, 1),
    ("гречка", FoodType.main_course, 1),
    ("рис", FoodType.main_course, 1),
    ("рис с маслом", FoodType.main_course, 1),
    ("куриные треугол", FoodType.garnish, 1),
    ("зразы с мясом", FoodType.garnish, 1),
    ("нагетсы", FoodType.garnish, 0.8),
    ("котлета куриная", FoodType.garnish, 1),
    ("котлета по-киевски", FoodType.garnish, 1),
    ("эскалоп с овощами", FoodType.garnish, 1),
    ("эскалоп под сыроми", FoodType.garnish, 1),
    ("говядина в соусе", FoodType.garnish, 1),
    ("филе куриное с помидором", FoodType.garnish, 1),
    ("голубцы с мясом и рисом", FoodType.garnish, 0)
]

menu_plans = [
    [FoodType.appetizer, FoodType.main_course, FoodType.garnish],
    [FoodType.main_course, FoodType.garnish, FoodType.garnish]
]

user_char = "P"