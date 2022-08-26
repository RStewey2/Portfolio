# Nested Loop Iteration with User Input

def Main():

#print start of program

    print("This program will calculate the total amount of rain, given the number of years. Follow each instruction and hit enter.")

# get number of years from the user

    year_count = int(input("Enter the number of years: "))

# initialize total_rain 

    total_rain = 0.0

# start year loop

    for i in range(1,(year_count+1)):

# start month loop

        for k in range(1,13):

# get current month's rain amount and add it to total_rain
            month_rain = float(input("Enter the number of inches of rain for month "+ str(k) + " for year " + str(i) + ": "))
            total_rain += month_rain

# print the results
    print("Number of Months: " + str(12 * year_count))
    print("Total amount of rain (inches): " + str(total_rain))
    print("The average rain per month is " + str("{:.2f}".format(total_rain/(year_count*12))) + " inches")

#offer to start a new calculation
    print("Do you want to make another calculation?")
    usr1 = input("Y/N: ")
    if usr1.upper() == "Y":
        Main()
    else:
        print("Thank you!")

Main()
