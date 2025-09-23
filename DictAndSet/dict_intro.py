vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can_am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford FIesta Ghia 1.4',
    'roadster': 'Triumph Street Triple'
}

# my_car = vehicles['fiesta']
# print(my_car)

# commuter = vehicles['virago']
# print(commuter)

# learner = vehicles.get("er5")
# print(learner)

# for key in vehicles:
#     print(key, vehicles[key], sep=",")

# Adding items to out dictionary
vehicles['starfighter'] = 'Lockheed F-104'
vehicles['learjeet'] = 'Bombardier Learjeet 75'
vehicles['toy'] = 'glider'

# Updating items in our dictionary
vehicles["virago"] = "Yamaha XV535"

for key, value in vehicles.items():
    print(key, value, sep=", ")