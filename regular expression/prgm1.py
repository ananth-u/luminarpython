#regular expression
#pattern matching

#step 1:
#package not in bultins.py it is in re

import re
matcher=re.finditer("ab","abababababab")

cnt=0
for match in matcher:
    print(match.start())
    print(match.group())
    cnt+=1
print(cnt)
