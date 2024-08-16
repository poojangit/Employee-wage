import random

empDetails = [
    {
        'empId': 1,
        'empName': "Pooja",
        'attendance': ""
    },
    {
        'empId': 2,
        'empName': "Bhuvan",
        'attendance': ""
    },
    {
        'empId': 3,
        'empName': "Preethi",
        'attendance': ""
    }
]

def welcome_message():
    print("Welcome to Employee wage computation program")
    
def generate_random_number(): 
    return random.randint(0,2)

def daily_wage_computation(employee):
    
    wagePerHour = 20
    fullDayHour = 8
    partTimeHour = 4
    dailyWage = 0
    
    attendance = generate_random_number()
    if attendance == 0:
        employee['attendance'] = "Absent"
    elif attendance == 1:
        employee['attendance'] = "Part-time"
        dailyWage = wagePerHour * partTimeHour
    else: 
        employee['attendance'] = "Full-time"
        dailyWage = wagePerHour * fullDayHour
        
    return dailyWage
       

def montly_wage_computation(): 
    
    workingDays = 20
    
    for employee in empDetails:
        monthlyWage = 0
        for day in range(workingDays) :
            dailyWage = daily_wage_computation(employee)
            monthlyWage += dailyWage
        # print(f"Daily Wages of {employee['empName']} : {dailyWage}")
        print(f"Montly wages of {employee['empName']} for {workingDays} days: {monthlyWage}")
        print(employee)
            
if __name__ == '__main__' :
    welcome_message()
    montly_wage_computation()
        