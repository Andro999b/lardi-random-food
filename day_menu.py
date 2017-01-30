# coding: utf-8

import config
import random
from fuzzywuzzy import fuzz


def plan(available_food, perception):
    # search foods and map them by type
    found_food = {type: [] for type in config.FoodType}
    for food_name in available_food:
        best_score = 0
        best_matches = []
        for pf in config.prefered_food:
            if pf[2] == 0:
                continue

            score = fuzz.ratio(pf[0], food_name)
            if best_score < score:
                best_matches = [pf]
                best_score = score
            elif best_score == score:
                best_matches.append(pf)

        # filter by min score
        if best_score > config.minimal_similarity:
            chosen_food = random.choice(best_matches)
            food_type = chosen_food[1]
            found_food[food_type].append((food_name, chosen_food))

    # sort each type by prefer
    for food_by_type in found_food.values():
        food_by_type.sort(key=lambda item: item[1][2], reverse=True)

    result_plans = []
    for food_plan in config.menu_plans:
        planned = set()
        summary_score = 0
        for foot_type in food_plan:
            best_score = 0
            best_matches = []

            for food in found_food[foot_type]:
                if food[0] in planned:
                    continue

                score = food[1][2]
                if score > best_score:
                    best_score = score
                    best_matches = [food[0]]
                elif score == best_score:
                    best_matches.append(food[0])
                else:
                    break

            if best_matches:
                summary_score += best_score
                planned.add(random.choice(best_matches))

        result_plans.append((summary_score, planned))

    # sort by score
    result_plans.sort(key=lambda item: item[0], reverse=True)
    # top scored plans
    top_score = result_plans[0][0]
    # similar plans
    winning_plans = [p for p in result_plans if (top_score - p[0]) <= perception]

    return random.choice(winning_plans)


