#Expense Tracker:

print('='*30)
print('Expense Tracker')
print('='*30)


Expenses = []
Total_Income = 0
print('1. Total Income\n',
      '2. Add Expenses\n',
      '3. View History\n',
      '4. Balance\n',
      '5.Exit')


def Exp():

    while True:
        Choice = input('Enter the selection (1-5) or type exit:')
        
        if Choice == 'exit' or Choice == '5':
            print("Thank you!")
            break

        elif Choice == '1':
            Total_Income = int(input('Enter the Total Income per Month:'))
            print(Total_Income)

        elif Choice == '2':
            item = input('Enter the Expense Name: ')
            amount = float(input('Enter the Amount: '))
            expense_dict = {'item': item, 'amount': amount}
            Expenses.append(expense_dict)
            print('Expenses Added successfully!')
            
        elif Choice == '3':
            print('Overall Expenses:',(Expenses))

            if not Expenses:
                print('No Expenses have been allocated')

            else:
                for E in Expenses:
                    print(E['item'], ':', E['amount'])
                print('Total Expenses:', sum (E['amount']for E in Expenses))
                

        elif Choice == '4':
            total_expense = sum(E['amount'] for E in Expenses)
            Balance = Total_Income - total_expense
            print('The Balance is:',Balance)

        else:
            print('INVALID CHOICE')
            break
        
    

Exp()
