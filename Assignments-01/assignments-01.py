"""ASSIGNMENTS 01
Student Grade Calculation Program
Content:
- Get name-surname, midterm exam score, final exam score and course attendance information from the user.
  Calculate the final course grade through using these data and the percentages.
Method:
- Exam scores and class attendance score range between 0-100.
- The total number of classes that a student should attend is 20.
5 points will be deducted for each missing class.
(For example: The course attendance score of a student who misses 3 classes: 100-(3x5)=85)
Percentages:
- Midterm exam score: 30%
- Final exam score: 50%
- Course attendance score: 20%
Result:
* Print the name-surname, midterm and final exam scores, course attendance information and final course grade of a
student on the screen."""

##############################################################################
# import random
# name, surname = input('what is yor name and surname:').split()
# midterm_exam_score = random.randint(1, 101)
# final_exam_score = random.randint(1, 101)
# course_attendance = 100 - random.randint(1, 21) * 5
# final_course_grade = midterm_exam_score * 0.3 + final_exam_score * 0.5 + course_attendance * 0.2
# print(f'name: {name}\n'
#       f'surname: {surname}\n'
#       f'midterm: {midterm_exam_score}\n'
#       f'final: {final_exam_score}\n'
#       f'courseAttendance: {course_attendance}\n'
#       f'finalCourseGrade: {final_course_grade}')
##############################################################################
# 2- INTEREST CALCULATION PROGRAM
#     Content:
# Receive the necessary input from the user and calculate the interest for a given principal amount, time and interest rate.
# Method:
# To be able to successfully run the program, you are required to receive the following information from the user:
# -Principal amount
# -Period of Time (year)
# -Rate of interest
# Interest Calculation Formula:
# Principal Amount X
# (Principal Amount) x (Period of Time (year)) x (Rate of Interest) / 100
# Result:
# After having the program calculate the interest, print out the total interest;
# average monthly interest and average daily interest; total balance (total interest + principal amount).

##############################################################################
# principalAmount, periodOfTime, rateOfInterest = input(
#     'Please enter value between space \nPrincipal amount\nPeriod of Time (year)\nRate of interest:').split()
# interest = int(principalAmount) * int(periodOfTime) * int(rateOfInterest) / 100
# print(f'Interest :{interest}\n'
#       f'Average monthly Interest: {interest / 12:04.2f}\n'
#       f'Average Daily Interest: {interest / 3650:04.2f}\n'
#       f'Total Balance: {(interest + int(principalAmount)):04.2f}\n')
##############################################################################
# 3- Monthly expenses calculation program
# Content:
# Write a program that rates the monthly expenses to the income and print the result.
# Method:
# 	Make calculations by getting the  following expenses from the user:
# 		-kitchen
# 		-education
# 		-clothing
# 		-transportation

# income = float(input('aylik gelirinizi giriniz:'))
# kitchenExpenses = float(input('mutfak giderini giriniz:'))
# educationExpenses = float(input('egitim giderini giriniz:'))
# clothingExpenses = float(input('giyim giderini giriniz:'))
# transportExpenses = float(input('ulasim giderini giriniz:'))
# totalExpenses = kitchenExpenses + educationExpenses + clothingExpenses + transportExpenses
#
# kitchenExpRate = '{:04.2f}'.format(kitchenExpenses / totalExpenses)
# educationExpRate = '{:04.2f}'.format(educationExpenses / totalExpenses)
# clothingExpRate = '{:04.2f}'.format(clothingExpenses / totalExpenses)
# transportExpRate = '{:04.2f}'.format(transportExpenses / totalExpenses)
# incomeExpensesRate = '{:04.2f}'.format(income / totalExpenses)
# print(f'total cost of the person whose information is entered {totalExpenses}'
#       f'income/expense ratio{incomeExpensesRate}')
# f = open('expenses', 'w')
# print(f'EXPENSES\n'
#       f'bilgileri girilen kisinin toplam masrafi {totalExpenses}\n'
#       f'mutfak_gideri:{kitchenExpenses} mutfak_gider_orani: {kitchenExpRate}\n'
#       f'egitim_gideri: {educationExpenses} egitim_gider_orani: {educationExpRate}\n'
#       f'giyim_gideri:{clothingExpenses} giyim_gider_orani: {clothingExpRate}\n'
#       f'ulasim_gideri:{transportExpenses} ulasim_gider_orani: {transportExpRate}\n'
#       f'gelirinin gidere orani {incomeExpensesRate}dir\n', file=f)
##############################################################################
# 4-  User Name and Password Character Control
# Ask the user to create a user name composed of 3-18 characters. If the user name includes a number,
# then warn the user that a user name cannot include a number. After that, ask the user to create a password composed of
# 6-12 characters. If the number of characters in the password is less than 6 or more than 12, then warn the user.
# If both the user name and password meet the conditions, then print the user name and password on the screen.
##############################################################################
# while True:
#     username = input("enter user name composed of 3-18 characters:")
#     if any(i.isdigit() for i in username):
#         print('You cannot use numbers in username')
#     elif len(username) <= 3 or len(username) >= 18:
#         print('Username can be 3 to 18 characters')
#     else:
#         print('Username successfully created')
#         while True:
#             password = input('Please enter a password composed of 6-12 characters')
#             if len(password) <= 6 or len(password) >= 12:
#                 print('Username can be 6-12 characters')
#             else:
#                 print(f'Username: {username}\nPassword: {password}')
#                 break
#     break
##############################################################################
# 5- FIZZ BUZZ
# Print the numbers between 1-100. But instead of the numbers that can be divided by 3 you must print the word FIZZ,
# instead of the numbers that can be divided by 5 you must print the word BUZZ and  for the ones can be divided by
# both 3 and 5 you must print FIZZBUZZ.
##############################################################################
# number = 1
# while number < 100:
#     if number % 15 == 0:
#         print('FIZBUZZ')
#     elif number % 3 == 0:
#         print('FIZZ')
#     elif number % 5 == 0:
#         print('BUZZ')
#     else:
#         print(number)
#     number += 1
##############################################################################
# 6- PRIME NUMBERS
# Write a program that controls if the number entered by the user is prime number or not.
##############################################################################
# def isPrime(num):
#     if num == 1:
#         return False
#     elif num == 2:
#         return True
#     else:
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True
#
#
# while True:
#     number = input('number:')
#     if number == 'q':
#         break
#     else:
#         number = int(number)
#         if isPrime(number):
#             print(number, 'is prime')
#         else:
#             print(number, 'is not prime')
# ##############################################################################
# 7- NUMERICAL GRADE TO LETTER GRADE CONVERSION
# A	90-100
# B	80-89
# C	70-79
# D	60-69
# F	< 60
# 1-Ask the user to enter the name of the course he/she wants to convert grades
# Save the course name into a variable
# 2-Ask the user to enter his/her numerical grade for the course
# 3-Convert the numerical grade to letter grade according to the table above
# 4-Print course name and letter grade for the course
# 5-After printing the course, ask the user if he/she wants to continue converting grades for
# another course ('y' or 'Y') or exit entering a certain character such as 'q' or 'Q'.
# 5-Return the step 1 if entered 'y' or 'Y' or exit if 'q' or 'Q' is entered.
##############################################################################
# while True:
#     courseName = input('course name: ')
#     grade = int(input(f'wat is the grade {courseName}: '))
#     if grade >= 90:
#         grade = "AA"
#     elif grade >= 80:
#         grade = "BB"
#     elif grade >= 70:
#         grade = "CC"
#     elif grade >= 60:
#         grade = "DD"
#     else:
#         grade = "FF"
#     print(f'course name:{courseName}\n'
#               f'courseGrade : {grade}')
#     answer = input("what do you want\n"
#                    "converting grades for another course enter 'y' or 'Y'\n"
#                    "exit entering a certain character such as 'q' or 'Q'\n").lower()
#     if answer == 'y':
#         continue
#     elif answer == 'q':
#         break
#     break
