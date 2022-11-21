#define Employee management system program. 
def EmployeeManagementSystem():
    #create employeesInfo list
    employeesInfo = []
    #define export option
    def exportInfo():
        #create writtable .txt file
        employeeFile = open("Employee Management.txt","w")
        #employee info is written to .txt in single line
        for i in range(0,len(employeesInfo)):
            employeeline = employeesInfo[i][0] + " " + employeesInfo[i][1] + " " + employeesInfo[i][2] + " " + employeesInfo[i][3] + " " + employeesInfo[i][4]
            employeeFile.write(employeeline + "\n")
        employeeFile.close()
    #employee info is stripped of unnecassary spaces and characters, and each line item is assigned to corresponding info. I.E. SSN, Name, etc. 
    def importInfo():
        employeesInfo.clear()
        employeeFile = open("Employee Management.txt","r")
        for line in employeeFile:
            strippedLine = line.strip()
            employeeByLine = strippedLine.split()
            employee = [employeeByLine[0]+ " " + employeeByLine[1],employeeByLine[2], employeeByLine[3], employeeByLine[4], employeeByLine[5]]
            employeesInfo.append(employee)
        employeeFile.close()
    #removed option_2 prompt and renamed functionality 2 to add_employee to streamline program.
    def addemployee():
        employeeName = input("Employee Name: ")
        employeeSSN = input("Employee SSN: ")
        employeePhone = input("Employee Phone: ")
        employeeEmail = input("Employee Email: ")
        employeeSalary = input("Employee Salary: ")
        employee = [employeeName, employeeSSN, employeePhone,employeeEmail, employeeSalary]
        employeesInfo.append(employee)
    #define view_employee script
    def viewemployee(employeeName, employeeSSN, employeePhone, employeeEmail, employeeSalary):
        print("-"*10 ,employeeName, "-"*10)
        print("Employee SSN:", employeeSSN)
        print("Employee Phone:", employeePhone)
        print("Employee Email:", employeeEmail)
        print("Employee Salary:", employeeSalary)
        print("\n")
    #updated functionality4 to functionality5 due to the additions of export info and import info.
    def functionality5():
        print("-"*58)
        numEmployees = len(employeesInfo)
        print("           There are (" + str(numEmployees)+") employees in the system.\n")
        print("-"*58)
        print("To add a new employee enter 1. \nTo view all employees enter 2.   \nTo search for employee by SSN enter 3. \nTo edit employee information enter 4. \nTo export employee info to file enter 5.  \nTo import employee information enter 6. \nTo exit enter 7. ")
        print("-"*58)
        option_1 = int(input("Please enter your option number: "))
        #If 1 is selected the add_employee script is ran
        if option_1 == 1:
            addemployee()
            functionality5()
        #viewemployee script is ran if option 2 is selected to display all employees
        elif option_1 == 2:
            for employee in employeesInfo:
                employeeName = employee[0]
                employeeSSN = employee[1]
                employeePhone = employee[2]
                employeeEmail = employee[3]
                employeeSalary = employee[4]
                viewemployee(employeeName, employeeSSN, employeePhone, employeeEmail, employeeSalary)
            functionality5()
        #Viewemployee script is ran again. This time it only displays the specific employee pulled by SSN.
        elif option_1 == 3: 
            employeeSSN = input("Enter Employee SSN: ")
            for employee in employeesInfo:
                if employee[1] == employeeSSN:
                    employeeName = employee[0]
                    employeeSSN = employee[1] 
                    employeePhone = employee[2]
                    employeeEmail = employee[3]
                    employeeSalary = employee[4]
                    viewemployee(employeeName, employeeSSN, employeePhone, employeeEmail, employeeSalary)
            functionality5()
          #Input to look up employeeSSN then remove and add updated employee info.
        elif option_1 == 4:
            employeeSSN = input("Enter Employee SSN: ")
            for employee in employeesInfo:
                if employee[1] == employeeSSN:
                    employeesInfo.remove(employee)
                    addemployee()
            functionality5()
          #If 5 is selected, the exportInfo script is ran, which is defined above  
        elif option_1 == 5:
            exportInfo()
            functionality5()
        #If 6 is selected, the importInfo script is ran. Importing info from .txt file. 
        elif option_1 == 6:
            importInfo()
            functionality5()
        #Goodbye message for users wanting to exit system. 
        elif option_1 == 7:
          print("Goodbye!")
    functionality5()

EmployeeManagementSystem()
