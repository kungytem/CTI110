# CTI-110
# P3HW1 - Color Mixer
# Migle Kungyte
# 07/01/2020

# Ask user to enter first primary color.
PrimaryColor1 = input ('Please enter primary color 1: ')

# Ask user to enter second primary color.
PrimaryColor2 = input ('Please enter primary color 2: ')

# When you mix primary colors red and blue it dispalys purple.
if (PrimaryColor1 == 'red' and PrimaryColor2 == 'blue' ) or \
    (PrimaryColor1 == 'blue' and PrimaryColor2 == 'red' ):
    print( PrimaryColor1 + ' mixed with ' + PrimaryColor2 + ' is purple ' )

# When you mix primary colors red and yellow it displays oange.
elif (PrimaryColor1 == 'red' and PrimaryColor2 == 'yellow' ) or \
     (PrimaryColor1 == 'yellow' and PrimaryColor2 == 'red' ):
        print( PrimaryColor1 + ' mixed with ' + PrimaryColor2 + ' is orange ' )

# When you mix primary colors blue and yellow it displays green.
elif (PrimaryColor1 == 'blue' and PrimaryColor2 == 'yellow' ) or \
     (PrimaryColor1 == 'yellow' and PrimaryColor2 == 'blue' ):
        print( PrimaryColor1 + ' mixed with ' + PrimaryColor2 + ' is green ' )

# If at least one of entered colors is or a primary color then it displays that one ofentered colors is not a primary color.
else:
    print( 'At least one of your colors, ' + PrimaryColor1 + ' or ' + \
           PrimaryColor2 + ', is not a primary color')
