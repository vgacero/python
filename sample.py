country = "PHILIPPINES"
print("Mabuhay " + country)

edad = 54
if (edad > 10 and edad <= 15):
    print("Midget Division")
elif (edad > 15 and edad <= 20):
    print("Junior Division")
elif (edad > 20 and edad <= 30):
    print("Senior Division")
elif (edad > 30 and edad <= 40):
    print("Balik-Laro Division")
else:
    print("Sorry you are not allowed to play!")

cntr=''
counter = 9
while (counter != 0):
    cntr = cntr + ' ' + str(counter)
    counter=counter-1
print(cntr)