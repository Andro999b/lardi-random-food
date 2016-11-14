# coding: utf-8

import config
import random
from fuzzywuzzy import fuzz


def plan(available_food, perception):
    # score all available foods by prefered
    scored_food = []
    for food_name in available_food:
        best_score = 0
        last_best = None
        for pf in config.prefered_food:
            score = fuzz.ratio(pf[0], food_name) * pf[2]
            if best_score < score or (best_score == score and random.random() > 0.5):
                last_best = pf
                best_score = score

        # print(best_score, food_name)
        scored_food.append((food_name, last_best[1], best_score))

    scored_food.sort(key=lambda item: item[2], reverse=True)  # sort by score

    # search menu plan with highest score
    result_plans = []
    for food_plan in config.menu_plans:
        planned = set()
        summary_score = 0
        for ft in food_plan:
            best_score = 0
            last_best = None
            for sf in scored_food:
                if sf[0] in planned:
                    continue

                if sf[1] == ft:
                    # if food have equal score then choose randomly
                    if best_score < sf[2] or (best_score == sf[2] and random.random() > 0.5):
                        last_best = sf[0]
                        best_score = sf[2]

            summary_score += best_score
            planned.add(last_best)

        result_plans.append((summary_score, planned))

    # sort by score
    result_plans.sort(key=lambda item: item[0], reverse=True)

    top_score = result_plans[0][0]
    winning_plans = [p for p in result_plans if (top_score-p[0]) <= perception]

    return random.sample(winning_plans, 1)[0]


