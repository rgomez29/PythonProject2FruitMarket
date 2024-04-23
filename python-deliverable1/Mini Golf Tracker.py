# Intro to Mini Golf Program, prompt user for name and store variable
user_name = input("Welcome to Grand Circus Mini Golf! What is your name?")

# Greet user with input variable, ask how many rounds of golf
while True:
     num_rounds = (input(f"Hi {user_name} !  Do you want to play 6 or 3 holes today?"))
     if num_rounds in ['6', '3']:
         num_rounds = int(num_rounds)
         break
     else:
           print("Enter either '6' or 3")

# Create variable to the score at each hole
hole_scores = []

# create loop, either 3 or 6 times depending on user answer
for hole_number in range(1,num_rounds + 1):
    while True:
        try:
            putts = int(input(f"How many putts for hole {hole_number}?"))
            if putts < 0:
                print("Please enter a non-negative number of puts.")
            else:
                hole_scores.append(putts)
                break
        except ValueError:
            print("Please enter a valid integer.")

# store the cumulative total of putts for all holees
total_score = sum(hole_scores)

#create course par variable
course_par = 3 * num_rounds

# configure score output depending on user score, relative to course par
score_difference = course_par - total_score
if score_difference == 0:
    print(f"Good game, {user_name}! Your scored exactly the course par of {total_score}!")
elif score_difference < 0:
    print(f"Good game, {user_name}! You scored {total_score} which is {-score_difference} under the course par of {course_par}!")
else:
    print(f"Good game, {user_name}! You scored {-total_score} which is {abs(score_difference)} over the course par of {course_par}!")
