# Monte Carlo for Street Fighter 6 tournament duration

This little project aims to help Street Fighter 6 tournament
organizers with choosing between a *best of 3* (bo3) or *best of 5*
(bo5) format: 
either the winner is decided from 3 games or 5.

Fighting games tournaments are generally in the bo3
or bo5 format as explained before. The bo3
format has the reputation to be quicker, but competitors as well as 
the public seem to prefer the bo5 format, which favors 
the adaptation of players, and creates more impressive comebacks. 

We provide tools to compute the average duration of a tournament
in each format, as well as tools to compute the duration
between two phases, for example, between from top 512 to top 64.

The duration $X$ of each game is simulated by a normal variable (values are seconds):

$$ X \sim \mathcal{N}(35, 10) $$

which is based on empirical observation. 

Functions used for the simulation are in the 'functions.py' file.
You can directly run the 'simulation.py' file for results, and adjust to your needs !

### Requirements

A requirements.txt file is given. Functions only use numpy. 
