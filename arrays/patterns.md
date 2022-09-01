# Here are some of the patterns ideas aggregated from many array/sequence problems
- Prefix sums might be useful
- Usually in array problems there are 2 cases:
1) Do all the hard work/calculations in side of for loop, by dynamically updaing/storing/handling data. This way complexity will probably increase more than O(N) order.
2) Do some pre-work in one for loop(O(N)) and on another/or several additional loops do some calculation work. This way total complexity's order stays the same