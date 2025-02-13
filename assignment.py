#Updated 1 Feb 2025
#Create a program that will ask the user for a number between 1 and 12. You may assume the input is correct.
#After getting the number display which season it is. The ranges are:
#Spring: 3,4,5
#Summer: 6,7,8
#Fall: 9,10,11
#Winter 12,1,2
#Here is a sample output:
#What month is it? (1-12): 2
#The current season is Winter.
#For an extra 2 points, display the month as all. So the output becomes:
#What month is it? (1-12): 2
#The month is February and the current season is Winter.
#Remember to also complete the flowchart. It is strongly advised that you do the flowchart first,
#as this will help you write the code.

currentMonth = int(input("What month is it? (1-12): "))

monthsList = ["null", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
seasonsList = ["Spring", "Summer", "Fall", "Winter"]

month = monthsList[currentMonth]
#I read ahead a bit to figure this out, cause I knew picking from a list would be easier than making 12 different if statements. That being said, here's what that would look
#like, commented out and hidden.

#if currentMonth == 1:
#   month = "January"
#elif currentMonth == 2:
#   month = "February"
#elif currentMonth == 3:
#   month = "March"
#elif currentMonth == 4:
#   month = "April"
#elif currentMonth == 5:
#   month = "May"
#elif currentMonth == 6:
#   month = "June"
#elif currentMonth == 7:
#   month = "July"
#elif currentMonth == 8:
#   month = "August"
#elif currentMonth == 9:
#   month = "September"
#elif currentMonth == 10:
#   month = "October"
#elif currentMonth == 11:
#   month = "November"
#elif currentMonth == 12:
#   month = "December"
#else:
#   print("Error! That's not a month!")


if currentMonth == 3 or currentMonth == 4 or currentMonth == 5:
    season = "Spring"
elif currentMonth == 6 or currentMonth == 7 or currentMonth == 8:
    season = "Summer"
elif currentMonth == 9 or currentMonth == 10 or currentMonth == 11:
    season = "Fall"
else:
    season = "Winter"

#if month == 3 or month == 4 or month == 5:
#    season = "Spring"
#    if month == 6 or month == 7 or month == 8:
#        season = "Summer"
#        if month == 9 or month == 10 or month == 11:
#            season = "Fall"
#            if month == 12 or month == 1 or month == 2:
#                season = "Winter"

print(f"The month is {month} and the season is {season}.")