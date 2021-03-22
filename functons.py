def add_num(num1,num2):
    return num1+num2
result = add_num(10,20)  
print(result)  

##

def check_list(mylist):
    
  
    even_numbers = []
  
    for numbers in mylist:
        if numbers % 2 == 0:
            even_numbers.append(numbers)
        else:
            pass

    return even_numbers    
print(check_list([1,2,3,4,5]))

##


work_hours = [('Abby',100),('Sandy',300),('Maggie',900)]
    
def employee_check(work_hours):
    
    
    current_max = 0
    star_employee = ''
    
    for employee,hours in work_hours:
        
        if hours > current_max:
            current_max = hours
            star_employee = employee
        else:
            pass
            
    return(star_employee,current_max)
print(employee_check(work_hours))


            

    

