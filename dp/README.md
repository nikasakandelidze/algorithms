# Dynamic Programming framework

Dynamic programming is the algorithmic solution category that is concerned with maximization/minimization problems. DP problem has several properties:

- Optimal Substructure: a problem can be solved optimally if optimal solution can be created for all of it's sub-problems and thus deduct a final result.
  - This is true for both: Bottom-up and Top-down approach, since in both of the cases final result is dependant & calculated from the results of sub problems
- Overlapping sub-problems: In the dynamic programming usually it's the case that sub problems are being solved many times and that's why storing computation results in some storage(memoization, tabular) is always considered.

# Questions:

- How to decide on wether Bottom Up solution should use 1 or 2 dimensional array
- Is: "Creating array of all the possible variates of results from 0-N" a pattern common in most of DP problem solutions ( in bottom-up cases )?
- Is there a pattern for at first trying to solve for the most basic cases of inputs ( like when input(s) are 0 or something like that) and then building on top of that?

# One pattern of Tabular Dynamic Programming models

When you have some inputs ( capacity, strings, weight, etc) for tabular solution od DP you can generate all possible cases from simplest problem to existing(input) one. And gradually start solving from the simplest to the hardest problem. You'll need to base your harder problems on the solutions from the simpler ones using a recurrence relation.
