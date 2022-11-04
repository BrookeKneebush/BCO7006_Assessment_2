import csv #The csv module implements classes to read and write tabular data in CSV format.

#Emply lists created to append iterated items
manager_salaries = []
temp_salary = []

with open("employees.csv", "r", newline="") as csvfile: #Using the csv module, provided data is accessed
    reader = csv.DictReader(csvfile) #provided data is read
    for row in reader: #for loop iterating over instances in the data
        if row["employee_type"] == "Manager": #if loop filters only instances of employee_type "Manager"
            manager_salaries.append(int(row["salary"])) #for instances of "Manager," salary is appended to empty list
            average_manager_salary = round((sum(manager_salaries) / len(manager_salaries)), 2) #average salary of managers calculated
        for number in row["salary"]: #for loop to iterate over all instances in the data for "salary"
            temp_salary.append(int(row["salary"])) #salary instances appended to empty list as integers
        lowest_salary_dollars = min(temp_salary) #min function used to determine lowest of all salary instances
        if int(row["salary"]) == lowest_salary_dollars:
            lowest_salary_name = (row["first_name"] + " " + row["last_name"]) #name of employee with lowest salary concatonated

#f strings to print requested data
print("The average salary of managers is {:,.0f}".format(average_manager_salary), "dollars.")
print(lowest_salary_name, "has the lowest salary (${:,.2f}".format(lowest_salary_dollars) +").")
