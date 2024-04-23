import math

print('Hello console')

my_name = "Robert Gomez"
work_from_home = True
side = 15
radius = 10

print('Hello console')
print('My name is ' + my_name)
print('I work from home: ' + str(work_from_home))
print(f'The length of each side of the square is {side}')
print(f'The radius of the circle is {radius}')

square_area = side * side
square_perimeter = 4 * side
print(square_area)
print(square_perimeter)

circle_area = math.pi * radius * radius
print(f"The Square area is {circle_area}")

circle_perimeter = 2 * math.pi * radius
print(f"The Circle Perimeter is {circle_perimeter}")

# List of Travel Options

travel_options = ['foot', 'bike', 'car', 'airplane']
print("The travel options are:")
print(f"1){travel_options[0]}")
print(f"2){travel_options[1]}")
print(f"3){travel_options[2]}")
print(f"4){travel_options[3]}")


# Choose Travel Option
distance = 100
time = 0
cost = 0


travel_type = input('How would you like to travel?')
print("Travel Type:" + travel_type)

if travel_type == "foot":
    print("Walking is free! Speed is 3mph.")
    cost = 0
    time = distance / 3

elif travel_type == "bike":
   rent_bike = input("Do you need to rent the bike? (yes or no)")
   if rent_bike == "yes":
       print("Bike rental is $45! Speed is 10mphmph.")
       cost = 45
   else:
       print("Biking is free! Speed is 10mph.")
       cost = 0

   time = distance / 10

elif travel_type == "car":
     print("Driving is $0.25/mi. Speed is 60mph.")
     cost = 0.25 * distance
     time = distance / 60

elif travel_type == "airplane":
     passenger_count = int(input("How many passengers?"))
     cost = 0.10 * distance * passenger_count
     time = distance / 400

     print("Flying is $0.10/mi. Speed is 400mph.")
else:
     print(f"Sorry.{travel_type} is an invalid option.")



print(f"Traveling {distance} miles by {travel_type} took {time} hours and cost ${cost}")