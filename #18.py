#18

#Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No 
#Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes 
#Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
#Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
#The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
print('pls answer in yes or no')
x=input('are you vegan:')
y=input('are you vegitarian:')
z=input('are you gluten free:')
print()
#ive tried this multiple times but couldnt 
if x=='no'and y=='no' and z=='no':
    print('you can go to all resturants')
elif x=='no'and y=='yes' and z=='no':
    print('you can go to all resturants except Joes Burger')
elif x=='no'and y=='yes' and z=='yes':
    print('you can go to all resturants except Joes Burger and mamas fine italian')
elif x=='yes'and y=='yes' and z=='yes':
    print('you can only go to Corner Cafe and The Chefs Kitchen')
elif x == 'no' and y == 'no' and z == 'yes':
    print('You can go to Main Street Pizza Company and Corner Café')
elif x == 'yes' and y == 'no' and z == 'no':
    print('You can go to Corner Café')
elif x == 'yes' and y == 'no' and z == 'yes':
    print('You can go to Main Street Pizza Company, Corner Café, and The Chefs Kitchen')
elif x == 'yes' and y == 'yes' and z == 'no':
    print('You can go to Corner Café and The Chefs Kitchen')
else:
    print('look at the question')
