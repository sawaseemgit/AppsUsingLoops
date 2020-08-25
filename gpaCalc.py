# import math as m

print('Welcome to GPA Calculator App')
name = input('Whats is your name: ').title().strip()
no_Grades = int(input('How many grades will be entered: '))
grades = []
for i in range(no_Grades):
    grades.append(int(input(f'Enter grade-{i}: ')))

print('Grades sorted highest to lowest:')
grades.sort(reverse=True)
for grade in grades:
    print(f'\t{grade}')

average = round((sum(grades) / no_Grades), 2)
print(f"{name}'s Grade Summary:\n\t Total Number of Grades are:{no_Grades}\n"
      f"\tHighest Grade: {max(grades)}\n\tLowest Grade: {min(grades)}\n"
      f"\tGrades Average: {average}")

desired_avg = float(input('What is your desired average: '))
req_grade = desired_avg * (no_Grades + 1) - sum(grades)
req_grade = round(req_grade, 2)
print(f"In order to earn a {desired_avg} average, you will need to score "
      f"{req_grade} in your next assignment")
new_grades = grades[:]
print('Lets see whats your average grade if you enter a different grade.')
remove_grade = int(input('What grade would you like to change: '))
new_grade = int(input(f'What grade would you like to change {remove_grade} to: '))
new_grades.remove(remove_grade)
new_grades.append(new_grade)

print('New grades sorted highest to lowest:')
new_grades.sort(reverse=True)
for grade in new_grades:
    print(f'\t{grade}')

new_average = round((sum(new_grades) / no_Grades), 2)
print(f"{name}'s New Grade Summary:\n\t Total Number of Grades are:{no_Grades}\n"
      f"\tHighest Grade: {max(new_grades)}\n\tLowest Grade: {min(new_grades)}\n"
      f"\tGrades Average: {new_average}")

print(f'Your new average would be {new_average} compared to real average of {average}')
avg_change = round((new_average - average), 2)
print(f'That is change of {avg_change} points!!')

print('Too bad, your original grades are still the same:\n', grades, 'You need to '
                                                                     'ask for extra credit')