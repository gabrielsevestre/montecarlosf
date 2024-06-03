import numpy as np


#  This function computes the total number of games in a tournament with n_participants
def compute_n_total_sets(n_participants=512):
    assert np.log2(n_participants).is_integer(), ('Please enter a valid number of participants, '
                                                  'which must be a power of 2')
    winners_n_match = n_participants - 1
    losers_n_match = n_participants - 2
    # formulas below
    # z = int(np.log2(no_participants))
    # winners_no_match = sum([no_participants/2**k for k in range(1,z+1)])
    # losers_no_match = sum([2*no_participants/2**k for k in range(2, z+1)])
    total = winners_n_match + losers_n_match + 1 + np.random.randint(0, 1)  # grand final + random reset
    # total = winners_n_match + losers_n_match + 1 - 10  # no top 8
    return total


# this function computes the number of sets between a start and an end, for example, between top 128 and top 64
# the 'include_first' parameter is True if the first round of sets is played, where no one gets eliminated
def compute_n_sets(start=128, end=64, include_first=False):
    assert end > 0, 'end parameter must be at least 1'
    cond = [np.log2(start).is_integer(), np.log2(end).is_integer(), start > end]
    assert all(cond), 'Please enter a valid number of participants and start and end values, with start < end'

    n_sets = 0
    if include_first:
        n_sets += start / 2
    players_left = start
    k = 1
    while players_left > end:
        if players_left == 2:
            if end == 2:
                break
            else:
                n_sets += 1
                break
        n_sets += start / 2 ** (k + 1) + 2 * start / 2 ** (k + 1)
        k += 1
        players_left -= players_left / 2

    return int(n_sets)


# This function simulates the duration of a match
def simul_duration_match(form='bo5'):
    if form == 'bo5':
        n_games = np.random.randint(3, 6)
    elif form == 'bo3':
        n_games = np.random.randint(2, 4)
    else:
        raise ValueError("Select a format between form='bo5' or form='bo3'")

    time = 0
    for _ in range(n_games):
        n_rounds = np.random.randint(2, 4)
        for _ in range(n_rounds):
            t = int(np.random.normal(loc=35, scale=10))
            time += t

    return time


# this function computes the duration of a tournament
def simul_tournament(n_participants=512, form='bo5'):
    n_sets = compute_n_total_sets(n_participants)
    tot_time = 0
    for _ in range(n_sets):
        t = simul_duration_match(form)
        tot_time += t
    return tot_time


#  this function does the Monte-Carlo process to estimate the average duration of a tournament
def simul(n_sim=1000, n_participants=512, form='bo5'):
    esp = 0
    var = 0
    for _ in range(n_sim):
        t = simul_tournament(n_participants, form)
        esp += t
        var += t**2
    esp /= n_sim
    var = var/n_sim - esp**2
    std = 1.96*np.sqrt(var/n_sim)
    return esp, std


#  this function does the Monte-Carlo simulation to estimate the duration between two phases,
#  for example between top 128 and top 64
def simul_phase(n_sim=1000, start=128, end=64, include_first=False, form='bo5'):
    n_sets = compute_n_sets(start=start, end=end, include_first=include_first)
    esp = 0
    var = 0
    for _ in range(n_sim):
        duration = 0
        for __ in range(n_sets):
            duration += simul_duration_match(form=form)
        esp += duration
        var += duration**2
    esp /= n_sim
    var = var/n_sim - esp**2
    std = 1.96*np.sqrt(var/n_sim)
    return esp, std


# utility function to print times
def return_times(duration):
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    return hours, minutes, seconds
