
#   Have a global result list for all possible substrings
#   for each character in the string:
#       inner list of substrings
#       current=current character
#       add current to inner list
#       for all the rest of the characters:
#           append it to current
#           add current to the inner list
#       add all elements of inner list to global list
def generate_substrings(s):
    result = []
    for i in range(len(s)):
        current = s[i]
        substrings_from_curent = [current]
        for j in range(i+1, len(s)):
            current += s[j]
            substrings_from_curent.append(current)
        result += substrings_from_curent
    return result



s = "123" # 1, 2, 3, 12, 23, 123
substrs = generate_substrings(s)
print(substrs)
assert len(substrs) == 6
for i in ['1', '2', '3', '12', '23', '123']:
    assert i in substrs


