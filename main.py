from packages import beer
import json

x = beer.random(3)
print("RANDOM BEER SUGGESTION")
for i in range(3):
    print(json.dumps(x[i], indent=2))

print('---*---'*20, end='\n\n')

y = beer.suggest_beer(no_of_suggestion=3, abv_get = 6, abv_lt= 9)
print("SUGGESTION BASED ON YOUR CHOICE")
for i in range(3):
    print(json.dumps(x[i], indent=2))

