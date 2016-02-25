first_year_gpa=int(input('Please Enter First_Year_GPA:'))
second_year_gpa=int(input('Please Enter Second_Year_GPA:'))
increase=((second_year_gpa-first_year_gpa)/first_year_gpa)*100
print(increase)

print('%.1f%%' %increase)

# find the rate of increase in GPA from first year to second year! round up to 1 decimal