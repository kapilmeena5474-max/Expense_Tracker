#Projrct : Expense Tracker

Expenses= []
print("Welcome To Expense Tracker")

while True :
    print("====MENU====")
    print("1. Add expenses")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. EXIT")

    choice= int(input("Please Enter Ypur Choice : "))

#add Expenses
    if(choice == 1):
        date= input("Enter the DATE of Expenditure :")
        category= input("Enter the Category of your Expenditure :")
        description= input("Any detail you want to give :")
        amount= input("Enetr the amount :")

        expenseslist= {
            "DATE" : date,
            "Category" : category,
            "Description" : description,
            "Amount" : amount
        }

        Expenses.append(expenseslist)
        print("\n Expense is added SUCCESFULLY")

#View ALL EXPENSES
    elif(choice == 2):
        if ( len(Expenses)==0 ):
            print("No Expenses Till Now")
        else:
            print("==== Here's Your All Expenditure ====")
            count= 1  
            for eachExpenditure in Expenses:
                print(f"{count} ---> DATE : {eachExpenditure["DATE"]} ,/n  CATEGORY : {eachExpenditure["Category"]} ,/n   Description : {eachExpenditure["Description"]} ,/n    Amount {eachExpenditure["Amount"]}")   

#View Total Spending 
    elif(choice ==3):
        total=0
        for eachExpenditure in expenseslist:
            total = total + eachExpenditure["amount"]
        print("\n TOTAL EXPENDITURE = ", total)

#EXIT
    elif(choice== 4):
        print("THANK YOU")
        break

    else:
        print ('Invalid Choice , TRY AGAIN')



