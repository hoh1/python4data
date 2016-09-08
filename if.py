# make sure to do the tab after IF
# age = int(input('what is your age?'))
# if age >= 18:
#     print('your age is', age)
#     print('adult')
# else:
#     print('your age is', age)
#     print('teenager')
# if age >= 18:
#     print('adult')
# elif age >= 6:    
#     print('teenager')
# else:
#     print('kid')

# if 0:
#     print('True')
    
# BMI calculator    
weight =input('what is your weight:')
height =input('what is your height:')
weight =float(weight)
height =float(height)
BMI =weight/(height*height)
if BMI <=18.5:
    print('Under Weight') 
elif 18.5< BMI <=25:
    print('Normal Weight')
elif 25< BMI <= 29.9:
    print('Over Weight')
else:
    print('Obsese')    