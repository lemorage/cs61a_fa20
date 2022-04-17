"""
    This file contains your final_strategy that will be submitted to the contest.
    It will only be run on your local machine, so you can import whatever you want!
    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
"""

from hog import *

PLAYER_NAME = 'Almighty Lemorage'  # Change this line!


def final_strategy(score, opponent_score):
    if score <= 106:
        return extra_turn_strategy(score, opponent_score)     
    else:
        return bacon_strategy(score, opponent_score)
