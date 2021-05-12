import time
import os
naira = u"\u20A6"   ###########Naira code

# This is the function for delay the time
def new_func():
    def timing():
        time.sleep(2)
        print("===="*8, "\n" + "===="*8)
    return timing

timing = new_func()
        
class Budget(object):
    def __init__(self):
        os.system('cls') #This helps to clear the terminal anytime we restart or run the program
        self.budget = float(input("How much is your budget? \n"))
        # Calculating our Budget
        self.spending = self.budget * 0.5 #This allows half of the budget to go into spending categories
        # Calculating Budget Stops
        self.main()
        
    def main(self):
        os.system('cls')
        timing()
        print("Note: This calculator follows the 50-20-30 rule.")
        print("===="*8, "\n" + "===="*8)

        # This helps to format the amount {:.2f}
        print("Your total budget is: \n%s" % naira,'{:.2f}'.format(self.budget))
        print("===="*8, "\n" + "===="*8)

        # Given Users options to procede
        main_option = int(input("What do you want to do? \n " +
                                "1. View overall budget \n" +
                                " 2. View Spending budget \n"+
                                "====================================== \n"))
        if main_option == 1:
            timing()
            self.overall_budget()
        elif main_option == 2:
            timing()
            self.spending_budget()
        else:
            timing()
            quit

    # Overall Budget
    def overall_budget(self):
        os.system('cls')
        option = int(input('How much do you want to save? \n' 
                           '1. 20% \n' 
                           '2. 30% \n'
                           "====================================== \n"))
        if option == 1:
            timing()
            self.saving = 0.2
        elif option == 2:
            timing()
            self.saving = 0.3
        else:
            timing()
            print("Error: Please select only 1 or 2!")
        self.final_saving = self.budget *  self.saving #Budget multiply by Saving
        self.extra = self.budget - self.final_saving - self.spending
        print('Spending: %s'% naira,'{:.2f}'.format(self.spending),' \n To save: %s'% naira, '{:.2f}'.format(self.final_saving), '\n Extra: %s' % naira, '{:.2f}'.format(self.extra) )
        timing()
        os.system('pause') #This give a promt for continuity/ prompt user to press anykey before continue
        self.main()

    # Spending Budget Start Here
    def spending_budget(self):
        os.system('cls')
        print('Spending Budget: %s'% naira, '{:.2f}'.format(self.spending))
        timing()
        rent = float(input('Rent amount paid in a month: \n' + '===============================\n'))
        bills = float(input('Monthly bills in a month: \n ' + '===============================\n'))
        miscellaneous_expenses = self.spending - rent - bills
        print('EXPENSES: \n Rent: %s'% naira, '{:.2f}'.format(rent), '\n Bills: %s'% naira,'{:.2f}'.format(bills), '\n Miscellaneous Expenses: %s'% naira, '{:.2f}'.format(miscellaneous_expenses))
        time.sleep(2)
        os.system('pause')
        self.main()
    # Spending Budget Ends Here


        
Budget()