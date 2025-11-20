# 1.(Mandatory) Write a function called calculate_grade(score)
#    that RETURNS the correct letter grade:
#       90+ -> A
#       80-89 -> B
#       70-79 -> C
#       60-69 -> D
#       below 60 -> F
#
# 2. Write another function called display_report(score, grade)
#    that PRINTS something like:
#       Score: 85
#       Grade: B
#
# 3. In the main part of the program:
#       - ask the user for the score
#       - call calculate_grade(score)
#       - call display_report(score, grade)
#
# Keep input() outside the functions.

# Write your code here:
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 68 <= score <= 69:
        return "D"
    else:
        return "F"

def display_report(score, grade):
    print("score:", score)
    print("grade:", grade)

score = int(input("Enter the score: "))
grade = calculate_grade(score)
display_report(score, grade)