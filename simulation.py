from functions import simul, simul_phase, return_times


# print the results of the Monte-Carlo estimation
def print_results(n_sim=1000, n_participants=512):
    res_bo5 = simul(n_sim=n_sim, n_participants=n_participants, form='bo5')
    res_bo3 = simul(n_sim=n_sim, n_participants=n_participants, form='bo3')
    times_bo5 = return_times(res_bo5[0])
    times_bo3 = return_times(res_bo3[0])
    print(f"For {n_participants} players, with bo5 format, "
          f"tournament is {int(times_bo5[0])}h{int(times_bo5[1])}m{int(times_bo5[2])}s total +- {int(res_bo5[1])}s")
    print(f"For {n_participants} players, with bo3 format, "
          f"tournament is {int(times_bo3[0])}h{int(times_bo3[1])}m{int(times_bo3[2])}s total +- {int(res_bo3[1])}s")


# print the results of the Monte-Carlo simulation for a given phase
def print_results_phase(n_sim=1000, start=128, end=64, include_first=False):
    res_bo5 = simul_phase(n_sim=n_sim, start=start, end=end, include_first=include_first, form='bo5')
    res_bo3 = simul_phase(n_sim=n_sim, start=start, end=end, include_first=include_first, form='bo3')
    times_bo5 = return_times(res_bo5[0])
    times_bo3 = return_times(res_bo3[0])
    print(f"From top {start} to top {end}, with bo5 format, "
          f"tournament is {int(times_bo5[0])}h{int(times_bo5[1])}m{int(times_bo5[2])}s total +- {int(res_bo5[1])}s")
    print(f"From top {start} to top {end}, with bo3 format, "
          f"tournament is {int(times_bo3[0])}h{int(times_bo3[1])}m{int(times_bo3[2])}s total +- {int(res_bo3[1])}s")


if __name__ == '__main__':
    print_results()
    print_results_phase()