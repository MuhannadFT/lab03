employees = {}
while(True):
    name = input("Enter employee's name: ")
    if name == "no":
        break
    salary = float(input(str("Enter the salary of %s: " %name)))
    employees[name] = {salary}