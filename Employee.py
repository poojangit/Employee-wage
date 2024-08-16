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

def welcome_message() :
    print("Welcome to Employee wage computation program")
    
def generate_random_number() : 
    return random.randint(0,2)

def wage_computation():
    
    wagePerHour = 20
    fullDayHour = 8
    partTimeHour = 4
    
    for employee in empDetails:
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
            
        employee['daiyWage'] = dailyWage
        print(f"Daily Wages of {employee['empName']} : {dailyWage}")
        print(employee)

if __name__ == '__main__' :
    welcome_message()
    wage_computation()
        