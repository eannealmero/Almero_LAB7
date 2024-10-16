name = input("Enter name here: ")
section = input("Enter section: ")

# restriction of between 40 and 100
prelim = float(input("Enter Prelim grade: "))
if prelim < 40 or prelim > 100:
    print("Invalid input of grade, grade must be between 40 and 100")
   
else:
    midterm = float(input("Enter Midterm grade: "))
    if midterm < 40 or midterm > 100:
        print("Invalid input of grade, grade must be between 40 and 100")
        
    else: 
        final = float(input("Enter Final grade: "))
        if final < 40 or final > 100:
            print("Invalid input of grade, grade must be between 40 and 100")
            
        else:
            finalgrade = (prelim * 0.3333) + (midterm * 0.3333) + (final * 0.3333)
            final_grade = round(finalgrade)
            print(f"Your final grade is: {final_grade}")
            
            
#GPA equivalent            

        if 99 <= final_grade <= 100:
            print("Your GPA is 1.00")
    
        elif 96 <= final_grade <= 98:
            print("Your GPA is 1.25")   
    
        elif 93 <= final_grade <= 95:
            print("Your GPA is 1.50")
    
        elif 90 <= final_grade <= 92:
            print("Your GPA is 1.75")
    
        elif 87 <= final_grade <= 89:
            print("Your GPA is 2.00")
    
        elif 84 <= final_grade <= 86:
            print("Your GPA is 2.25")
    
        elif 81 <= final_grade <= 83:
            print("Your GPA is 2.50")
    
        elif 78 <= final_grade <= 80:
            print("Your GPA is 2.75")
    
        elif 75 <= final_grade <= 77:
            print("Your GPA is 3.00")
    
        elif final_grade <= 74:
            print("Your GPA is 5.0")
            
        else:
            print("Invalid input of grade, grade must be between 40 and 100")
    
