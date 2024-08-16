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
    hoursWorked = 0
    
    attendance = generate_random_number()
    if attendance == 0:
        employee['attendance'] = "Absent"
    elif attendance == 1:
        employee['attendance'] = "Part-time"
        dailyWage = wagePerHour * partTimeHour
    else: 
        employee['attendance'] = "Full-time"
        dailyWage = wagePerHour * fullDayHour
        
    return dailyWage, hoursWorked
       

def montly_wage_computation(): 
    
    workingDays = 20
    maxWorkingHours = 100
    
    for employee in empDetails:
        monthlyWage = 0
        totalHoursWorked = 0
        totalDaysWorked = 0
        
        # for day in range(workingDays) :
        #     dailyWage = daily_wage_computation(employee)
        #     monthlyWage += dailyWage
        # print(f"Daily Wages of {employee['empName']} : {dailyWage}")
        
        while totalDaysWorked < workingDays and totalHoursWorked < maxWorkingHours : 
            dailyWage, hoursWorked = daily_wage_computation(employee)
            monthlyWage = monthlyWage + dailyWage
            totalHoursWorked = totalHoursWorked + hoursWorked
            totalDaysWorked = totalDaysWorked + 1
            
            if totalHoursWorked >= maxWorkingHours:
                print(f"Reached max working hours of {maxWorkingHours} hours for {employee['empName']}")
                break
            if totalDaysWorked >= workingDays:
                print(f"Reached max working days of {maxWorkingHours} days for {employee['empName']}")
                break
            
        print(f"Montly wages of {employee['empName']} for {workingDays} days: {monthlyWage}")
        print(employee)
            
if __name__ == '__main__' :
    welcome_message()
    montly_wage_computation()
        