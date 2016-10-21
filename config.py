from enum import Enum


class FoodType(Enum):
    appetizer = 1
    main_course = 2
    garnish = 3
    desert = 4

# name, type, priority
prefered_food = [
    ("окрошка", FoodType.appetizer, 1),
    ("cуп гороховый", FoodType.appetizer, 1),
    ("пюре картофельное", FoodType.main_course, 1),
    ("гречка с маслом", FoodType.main_course, 1),
    ("рис", FoodType.main_course, 1),
    ("куриные треугол", FoodType.garnish, 1),
    ("зразы с мясом", FoodType.garnish, 1),
    ("нагетсы", FoodType.garnish, 0.8),
    ("котлета куриная", FoodType.garnish, 1),
    ("котлета по-киевски", FoodType.garnish, 1)
]

menu_plans = [
    [FoodType.appetizer, FoodType.main_course, FoodType.garnish],
    [FoodType.main_course, FoodType.garnish, FoodType.garnish]
]

user_char = "P"