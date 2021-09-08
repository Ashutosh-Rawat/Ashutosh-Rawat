class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        pass

    def amIOld(self):
        pass
        # Do some computations in here and print out the correct statement to the console

    def yearPasses(self):
        pass
        # Increment the age of the person in here


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")

# sample input
# 4
# -1
# 10
# 16
# 18
