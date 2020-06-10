import random
# # creates a new list then instiates 10 random numbers(between 1 and 5)
# my_randoms = list()
# for i in range(10):
#   my_randoms.append(random.randrange(1, 6))
# # creates a list of numbers 1-10
# numbers_1_to_10 = range(1,11)
# # loop over the numbers then loop over the randoms and if they match print it
# for number in numbers_1_to_10:
#     the_numbers_match = False

#     for i in my_randoms:
#         if i == number:
#             the_numbers_match = True

#     if the_numbers_match == True:
#         print(f'the list contains {number}')
#     else:
#         print(f'the list doesn\'t contain {number}')

planets_list = ["Mercury", "Mars"]
second_planet = planets_list[1]
# print("The second planet is %s" % second_planet)
# print(f"The second planet is {second_planet}")

planets_list.append("Jupiter")
planets_list.append("Saturn")

planets_list.extend(["Uranus", "Neptune"])

planets_list.insert(1, "Earth")
planets_list.insert(1, "Venus")

planets_list.append("Pluto")

rocky_planets = list()
rocky_planets = planets_list[0:4]

del planets_list[8]

print(planets_list)

spacecraft = [
    ("Pioneer 10", "Jupiter"),
    ("Pioneer 11", "Saturn"),
    ("Voyager 2", "Mars"),
    ("Voyager 1", "Mars"),
    ("Galileo", "Jupiter"),
    ("New Horizons", "Jupiter")
]

for planet in planets_list:
    has_visited = False
    a = f'{planet} was visited by '
    for tup in spacecraft:
        if tup[1] == planet:
            a += f'{tup[0]}, '
            has_visited = True
    else:
        a = a[slice(-2)] + f'.'

    if has_visited:
        print(a)
    else:
        print(f'Nobody visiting {planet}.')
