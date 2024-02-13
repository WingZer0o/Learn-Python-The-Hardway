people = 30
cars = 40
trucks = 15

if cars > people:
    print("We shoujld take the cars")
elif cars < people:
    print("We should not take the cars")
else:
    print("We cant't decide")

if trucks > cars:
    print("There's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's say home then.")