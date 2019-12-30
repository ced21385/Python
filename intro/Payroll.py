#Christopher Davis
#ITP 100 N01B
#11/6/2018
#B.Miller
#Payroll

#input the variables needed

empName = input("Enter an employee's name: ")

hours = eval(input("Enter in the number of hours worked in a week: "))

payRate = eval(input("Enter hourly pay rate: "))

federalTaxRate = eval(input("Enter federal tax withholding rate: "))

stateTaxRate = eval(input("Enter state tax withholding rate: "))

grossPay = float(hours * payRate)

federalTax = float(grossPay * federalTaxRate)

stateTax = float(grossPay * stateTaxRate)

#output the payroll statement

print("\n","\n","Employee Payroll Statement")
print(" --------------------------")
print("\n","\n",empName,"\n","\n")
print("Hours worked: ",hours)
print("Pay Rate: ",payRate)
print("Gross Pay: ", grossPay)
print("Federal Tax Withheld: ", federalTax)
print("State Tax Withheld: ", stateTax)
print("Net Pay: ", float(grossPay-federalTax-stateTax))