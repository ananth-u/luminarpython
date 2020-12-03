name=["a","b","c","d","e","f","g","h"]

passed=["a","b","c"]

stname=set(name)
stpass=set(passed)

diff=stname.difference(stpass)
print("failed studests", diff)