# Python program to determine the employee of a month based on max Working hours
def employee_check(abc):
    current_max = 0
    employee_of_month = ''

    for employee,hours in abc:
            if hours > current_max:
                    current_max = hours
                    employee_of_month = employee
            else:
                    pass
    return (employee_of_month,current_max)

work_hours = [('Abby',1000),('Billy',1000.0),('Cassie',800)]
result = employee_check(work_hours)
print(result)
