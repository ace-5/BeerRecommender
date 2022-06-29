from operator import lt
from packages import beer


answer = int(input("Do you want:\n0. Random Beer\n1. Specified Beer\nYour Choice => "))

if answer:
    abv_get = float(input("Specify minimum alcohol %: "))
    abv_lt = float(input("Specify maximum alcohol %: "))
    x = (beer.get_specified_beer(abv_get, abv_lt))
    for i in range(3):
        print(x[i])
    
else:
    x = beer.get_random_beer()
    for i in range(3):
        print(x[i])



