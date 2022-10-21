# Check multiple keys exists in a dictionary.
sports = {"python": 1, "django": 2, "rest api": 3}

# using comparison operator
print(sports.keys() >= {'python', 'rest api'})
print(sports.keys() >= {'django', 'mysql'})