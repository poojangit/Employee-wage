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
    
    for e in empDetails:
        attendance = generate_random_number()
        if attendance == 0:
            e['attendance'] = "Absent"
        else:
            e['attendance'] = "Present"
            
    for e in empDetails : 
        print(e)