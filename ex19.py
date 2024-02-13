def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheesses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")

print("We can just give the function number directly:")
cheese_and_crackers(20, 30)

print("Or, we can use variables for our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside:")
cheese_and_crackers(10 + 20, 5 + 6)

cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)