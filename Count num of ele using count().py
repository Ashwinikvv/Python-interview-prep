days = ['S','M','M','M','F','S']
y = set(days)

print([[x,days.count(x)] for x in y])

> [['M', 3], ['S', 2], ['F', 1]]
