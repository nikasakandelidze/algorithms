# Greedy algorithms

Greedy algorithms are types of algorithms that are intuitive and can be applied to some subset of optimization problems to calculate the min/max results without using dynamic programming or back tracking(recursive + re-evaluation)
So if we see somewhere that they are asking for min/max problem and these problem looks alike these famous greedy algorithmic problems we do try to think of greedy solution.

# Pattern of Greedy Algorithm

The pattern for greedy algorithm is to:

- Choose locally optimal solution in light of it leading to a globally optimal one
- Not back tracking or changing the decision after making it.

But as i understand we need to synthesize the property/function by which we aim to make local decisions:

- For activity selection: selecting Finish time
- For fractional knap-sack: Choosing the most costly materials first
- For coin change: Choosing the biggest coin first
  And this property/function should be found by reasoning, intuition and not some complex formulas or algorithmic techniques.
