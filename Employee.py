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
    return random.randint(0,1)

   

if __name__ == '__main__' :
    welcome_message()
    
    wagePerHour = 20
    fullDayHour = 8
    
    for employee in empDetails:
        dailyWage = 0
        attendance = generate_random_number()
        if attendance == 0:
            employee['attendance'] = "Absent"
        else:
            employee['attendance'] = "Present"
            dailyWage = wagePerHour * fullDayHour
            employee['daiyWage'] = dailyWage
            
        print(f"Daily Wages of {employee['empName']} : {dailyWage}")
    
        print(employee)