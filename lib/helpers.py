from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    pass


def find_department_by_name():
    pass


def find_department_by_id():
    pass


def create_department():
    pass


def update_department():
    pass


def delete_department():
    pass


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)



def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f'Employee {name} not found')



def find_employee_by_id():
    id_ = input("Enter the employee's ID: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f'Employee {id_} not found')



def create_employee():
    name = input("Enter the employee's name: ")
    department_id = input("Enter the employee's department ID: ")
    job_title = input("Enter the employee's job title: ")
    salary = input("Enter the employee's salary: ")

    try:
        employee = Employee.create(name, department_id, job_title, salary)
        print(f'Success: {employee}')
    except Exception as exc:
        print("Error creating employee: ", exc)



def update_employee():
    id_ = input("Enter the employee's ID: ")
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter the employee's new name: ")
            job_title = input("Enter the employee's new job title: ")
            salary = input("Enter the employee's new salary: ")

            employee.name = name
            employee.job_title = job_title
            employee.salary = salary
            employee.update()

            print(f'Success: {employee}')
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print(f'Employee {id_} not found')



def delete_employee():
    id_ = input("Enter the employee's ID: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(f'Employee {id_} not found')



def list_department_employees():
    department_id = input("Enter the department ID: ")
    employees = Employee.find_by_department(department_id)
    
    if employees:
        for employee in employees:
            print(employee)
    else:
        print(f'No employees found in department {department_id}')
