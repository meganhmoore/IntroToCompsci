class BankAccount:

#accounts={}

	def __init__ (self,name,balance):
		self.__accountName=name
		self.__totalBalance=balance

	def depositMoney(self):
		balance=float(input('How much would you like to deposit: '))
		self.__totalBalance+=balance

	def withdrawMoney(self):
		withdraw=float(input('How much would you like to withdraw: '))
		if self.__totalBalance-withdraw<0:
			print('You do not have this much money in your account.')
		else:
			self.__totalBalance-=withdraw

	def printBalance(self):
		print(self.__totalBalance)
#for num in range(100):
#	account=BankAccount()
#	accounts.append(account)
#for account in accounts:
#	accName=input('what is your name: ')
#	accNum=input('what is your account number: ')
#	if account.name=accName and account.number=accNum:
#		account=totalBalance
account=BankAccount('John',0)
choice=input('If you would like to deposit print "D", \n if you would like to withdraw print "W", \n if you would like to see your balance print "P", \n if you are done please print any other letter: ')
while choice =='D' or choice=='W' or choice=='P':
	if choice=='D':
		account.depositMoney()
		print('your balance is: ', account.printBalance())
		choice=input('If you would like to deposit print "D", \n if you would like to withdraw print "W", \n if you would like to see your balance print "P", \n if you are done please print any other letter: ')
	elif choice=='W':
		account.withdrawMoney()
		print('your balance is: ', account.printBalance())
		choice=input('If you would like to deposit print "D", \n if you would like to withdraw print "W", \n if you would like to see your balance print "P", \n if you are done please print any other letter: ')
	elif choice=='P':
		print('your balance is: ', account.printBalance())
		choice=input('If you would like to deposit print "D", \n if you would like to withdraw print "W", \n if you would like to see your balance print "P", \n if you are done please print any other letter: ')


print('your balance is: ', account.printBalance())


