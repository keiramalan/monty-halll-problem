# montys_problem.py
# Simulate Monty's problem
# Creators: Keira Malan and Annika Munro
# Date created: 19/05/20
# Last edited: 19/05/20

import random


def random_outcomes():
    """ function to create dictionary of 3
    values assigned with random booleans"""
    
    # create dictionary of 3 values with true, false, false
    outcome_1 = True
    outcome_2 = False
    outcome_3 = False
    outcome_list = [outcome_1, outcome_2, outcome_3]
    # shuffle list to ensure random outcome
    random.shuffle(outcome_list)
    # create dict with random booleans and return it
    outcome_dict = {1: outcome_list[0], 2: outcome_list[1], 3: outcome_list[2]}
    return outcome_dict
