def sort_employees(employees, sort_by):
    # Write your code here.
    new_employees = []
    if sort_by == "salary":
        new_employees = sorted(employees, key=lambda employ: employ[2])
    elif sort_by == "age":
        new_employees = sorted(employees, key=lambda employ: employ[1])
    else:
        new_employees = sorted(employees, key=lambda employ: employ[0])
        
    return new_employees