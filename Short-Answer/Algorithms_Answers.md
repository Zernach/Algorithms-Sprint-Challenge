#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^2)  —— one n in line one (below), and one n in line 2 (below) can be cancelled out

LINE 1 ——— while (a < n * n * n):
LINE 2 ———      a = a + n * n


b) O(log(n)) —— the amount of time diminishes due to j multiplied by two everytime


c) O(n) —— the function will linearly run as long as n is equal to

## Exercise II

"""
The following function should be used by architects who are planning
to consutruct on different planets in the solar system.

There have been too many suicides by jumping from buildings in this city.
We want to make that impossible to do from our planet's future buildings.

Here's what you do:
Submit how many floors you'd like your building to be (n_floor)
We'll conduct highly scientific egg dropping simulations on our remote servers.

If the egg doesn't break at the # of floors you're requesting, 
then we will consider it safe for you to construct on that planet.

However, if the egg breaks at the # of floors you're requesting to construct,
then we will tell you the highest # of floors that we WOULD consider safe for construction!
"""
def should_we_build_this_building(n_floor, f_floor = -1):

    broken = drop_egg(n_floor)

    if broken is True:
        f_floor += 1
        return should_we_build_this_building(f_floor, f_floor)

    else:
        return f"Safe to construct at {n_floor}!"
"""

Worst case scenario: it runs at an O(n-1) complexity, or rounded to O(n) runtime complexity.