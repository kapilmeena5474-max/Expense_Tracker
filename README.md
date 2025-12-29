# Expense Tracker
This is my first project.
____

## Table of content :
<a href="Overview">Overview</a><br>
<a href="Code">Code</a>
____

<h2><a class="anchor" id= "Overview"></a>Overview</h2>

This project is a "mini Expense tracker" throught which whenever the person do any expenditure then he have to provide basic detail of his Expenses (like Date, Category, Description, Amount). And at the end of the day He/She is able to View the total expenditure of the day.
____

<h2><a class="anchor" id= "Code"><a/>Code</h2>

Expenses= []<br>
print("Welcome To Expense Tracker")<br>
<br>
while True :<br>
    print("====MENU====")<br>
    print("1. Add expenses")<br>
    print("2. View All Expenses")<br>
    print("3. View Total Spending")<br>
    print("4. EXIT")<br>
<br>
    choice= int(input("Please Enter Ypur Choice : "))
<br>
#add Expenses<br>
    if(choice == 1):<br>
        date= input("Enter the DATE of Expenditure :")<br>
        category= input("Enter the Category of your Expenditure :")<br>
        description= input("Any detail you want to give :")<br>
        amount= input("Enetr the amount :")<br>
<br>
        expenseslist= {
            "DATE" : date,
            "Category" : category,
            "Description" : description,
            "Amount" : amount
        }
<br>
        Expenses.append(expenseslist)<br>
        print("\n Expense is added SUCCESFULLY")<br>
<br>
#View ALL EXPENSES<br>
    elif(choice == 2):
        if ( len(Expenses)==0 ):<br>
            print("No Expenses Till Now")<br>
        else:<br>
            print("==== Here's Your All Expenditure ====")<br>
            count= 1  <br>
            for eachExpenditure in Expenses:<br>
                print(f"{count} ---> DATE : {eachExpenditure["DATE"]} ,/n  CATEGORY : {eachExpenditure["Category"]} ,/n   Description :  {eachExpenditure["Description"]} ,/n    Amount {eachExpenditure["Amount"]}")  <br> 
<br>
#View Total Spending <br>
    elif(choice ==3):<br>
        total=0<br>
        for eachExpenditure in expenseslist:<br>
            total = total + eachExpenditure["amount"]
        print("\n TOTAL EXPENDITURE = ", total)

#EXIT
    elif(choice== 4):
        print("THANK YOU")
        break

    else:
        print ('Invalid Choice , TRY AGAIN')





