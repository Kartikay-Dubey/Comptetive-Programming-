# import re

# # Matches 'a' zero or more times
# pattern = r'a*'
# string = "1234abcabcabc123"
# matches = re.findall(pattern, string)

# print(matches)  # Output: ['', '', '', 'a', '', 'a', '', 'a', '', 'a', '', '']

# import re

# # Matches 'a' one or more times
# pattern = r'a+'
# string = "1234abcabcabc123"
# matches = re.findall(pattern, string)

# print(matches)  # Output: ['a', 'a', 'a']

import re

# Matches exactly 3 'a's
pattern = r'a{3}'
string = "1234abcabcabc123"
matches = re.findall(pattern, string)

print(matches)  # Output: []
