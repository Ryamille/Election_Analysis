print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1]== 'Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside"))
if temperature > 80:
    print("Trun on the Ac.")
else:
    print("Open the windowns")

#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of the counties.")
else:
    print("El Paso is not in the list of the counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")

#While Loop
#set variable x=0
x = 0
#test if les than or eqaul to five
while x <= 5:
    #if true we print x
    print(x)
    #increment x by 1
    x = x + 1
#condition is tested until false then loop stops

#i is used to indicate the index/values of the counties list
#inside range() length of the list of counties(3)
#i=0 so Arapahoe is printed
for count in counties:
    print(county)
for i in range(len(counties)):
    print(counties[i])
