
# It takes 2^N complexity to calculate all possible subsets of a set
def subset_sum(input, target):
    subset_sums = [0]
    # O(N)
    for current in input:
        # O(N)
        copy = [x+current for x in subset_sums[::]]
        subset_sums += copy
    return any(x == target for x in subset_sums)


def test_subset_sum():
    assert subset_sum([1, 2, 3, 4, 5, 6, 7], 3) is True
    assert subset_sum([1, 2, 3, 4, 5, 6, 7], 22) is True
    assert subset_sum([1, 2, 3, 4, 5, 6, 7], 10000) is False
    assert subset_sum([1, 2, 3, 4, 5, 6, 7], 100) is False


test_subset_sum()