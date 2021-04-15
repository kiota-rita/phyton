print("Your Savings Calculator\n") 

user_input = input("How much do you make per hour? ")
worked_hoursD = input("How many hours do you work per day? ")
worked_hoursW = input("How many hours do you work per week? ")
print("_________________________\n")

dayly_savings = int (user_input) * int(worked_hoursD) 
print("° This is your dayly saivings: ",dayly_savings,)

week_savings = dayly_savings*int(worked_hoursW)
print("° This is your weekly saivings: ", week_savings)

month_savings = week_savings * 4
print("° This is your monthly saivings: ", month_savings)