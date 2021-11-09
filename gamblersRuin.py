# The Gambler's Ruin
#   A gambler, starting with a given stake (some amount of money), and a goal
#   (a greater amount of money), repeatedly bets on a game that has a win probability
#   The game pays 1 unit for a win, and costs 1 unit for a loss.
#   The gambler will either reach the goal, or run out of money.
#   What is the probability that the gambler will reach the goal?
#   How many bets does it take, on average, to reach the goal or fall to ruin?

import random as random
import time as time

stake = 10        # Starting quantity of currency units
goal = 100        # Goal to reach in currency units
n_trials = 10000  # Number of trials to run
win_prob = 0.5    # Probability of winning an individual game


def gamble(cash, target_goal, win_probability):
    """
    A single trial of a gambler playing games until they reach their goal or run out of money.
    cash: the gambler's initial amount of currency units
    goal: the number of currency units to reach to be considered a win
    win_prob: the likelihood of winning a single game
    return: a tuple (outcome, bets):
        - outcome: the outcome of the trial (1 for success, 0 for failure)
        - bets: number of bets placed
    """

    # play games until the goal is reached or no more currency units remain
    bets = 0  # number of bets placed
    while 0 < cash < target_goal:
        bets += 1
        if random.random() < win_probability:
            cash += 1
        else:
            cash -= 1

    # return tuple of trial outcome, number of bets placed
    if cash == target_goal:
        return 1, bets
    else:
        return 0, bets


def display_gamble():
    print("\nQuestion 2: Gamblers Ruin\n")
    # run a number of trials while tracking trial wins & bet counts
    bets = 0  # total bets made across all games from all trials
    wins = 0  # total trials won
    start = time.time()  # time when we started the simulation
    for t in range(n_trials):
        w, b = gamble(stake, goal, win_prob)
        wins += w
        bets += b
    end = time.time()  # time when we stopped the simulation

    duration = end - start
    # display statistics of the trials
    print('Stake:', stake)
    print('Goal:', goal)
    print(str(100 * wins / n_trials) + '% were wins')
    print('Average number of bets made:',  str(bets / n_trials))
    print('Number of trials:', n_trials)
    print('The simulation took:', duration, 'seconds (about', n_trials/duration, 'trials per second)')
