#############################################################################################
################FIRST PYTHON BUILD, CALCULATOR PROGRAM#######################################
#############################################################################################
#useless program just for learning basics of python#
####################################################
################################################
####def of a couple of basic math fonction###
#############################################

def add(num1, num2):
	return num1 + num2
	
def sub(num1, num2):
	return num1 - num2

def mul(num1, num2):
	return num1 * num2

def div(num1, num2):
	return num1 / num2
	
def sqr(num1, num2):
	return num1 ** num2
	
def mod(num1,num2):
	return num1 % num2

	
###############################################################
##########################Main function########################
###############################################################

def main():

	###first python build, nuclearblast 2016######
	##############################################
	##First user need to choose operating langage
	run = "true"
	print('\n********PLEASE SELECT YOUR LANGUAGE********\n')
	lang = input('TYPE : en   to run in english \nTYPE : fr   to run in french\n')
	## French case ##
	if (lang == 'fr'): 
		print('\nLe programme est désormais en francais \n')
		print("Entrez x pour fermer le programme \n ")
		#usin variable run to repeat the program
		while (run == "true"):
			#error exceptation 
			try:
				op1 = input('Veuillez entrer le premier nombre \n')
				#if user type-in x set run to false
				if (op1 == "x"):
					run = "false"
				else:
					op3 = int(op1)
					op = input('Veuillez maintenant entrez un opérateur (+,-,/,*,**,%) \n')
					if (op == "x"):
						run = "false"
					elif (op == "+") or (op == "-") or (op == "/") or (op == "*") or (op == "**") or (op == "%"): 
						op2 = input('Entrez le deuxième nombre \n')
						if (op2 == "x"):
							run = "false" 
						##when the user type de correct information
						############################################
						else:
							op4 = int(op2) 
							if (op == "+"):
								sum = add(op3,op4)
								print(op3,op,op4,'=',sum,'\n')
							elif (op == "-"):
								sum = sub(op3,op4)
								print(op3,op,op4,'=',sum,'\n')
							elif (op == "/"):
								sum = div(op3,op4)
								print(op3,op,op4,'=',sum,'\n')
							elif (op == "*"):
								sum = mul(op3,op4)
								print(op3,op,op4,'=',sum,'\n')
							elif (op == "**"):
								sum = sqr(op3,op4)
								print(op3,op,op4,'=',sum, '\n')
							else:
								sum = mod(op3,op4)
								print(op3,op,op4,'=',sum, '\n')	
					else: 
						print("\n\nVous avez entrez un mauvais opérateur\n\n")
						pass
			except ValueError:
				print('\n\nVeuillez entrez un nombre entier\n\n')
				pass
	#english case
	elif(lang == 'en'):
		print('\nProgram will now run in english \n')
		print('Type x to close the program')
		while (run == "true"):
			try:
				op1 = input('Type the first number \n')
				if (op1 == "x"):
					run = "false"
				else:
					op3 = int(op1)
					op = input('Now type the operator (+,-,/,*,**,%) \n')
					if (op == "x"):
						run = "false"
					elif (op == "+") or (op == "-") or (op == "/") or (op == "*") or (op == "**") or (op == "%"): 
						op2 = input('Type the second number \n')
						if (op2 == "x"):
							run = "false" 
						else:
							op4 = int(op2) 
							if (op == "+"):
								sum = add(op3,op4)
								print(op3,op,op4,'=',sum,'\n')
							elif (op == "-"):
								sum = sub(op3,op4)
								print(op3,op,op4,'=',sum,'\n')
							elif (op == "/"):
								sum = div(op3,op4)
								print(op3,op,op4,'=',sum,'\n')
							elif (op == "*"):
								sum = mul(op3,op4)
								print(op3,op,op4,'=',sum,'\n') 
							elif (op == "**"):
								sum = sqr(op3,op4)
								print(op3,op,op4,'=',sum,'\n') 
							else:
								sum = mod(op3,op4)
								print(op3,op,op4,'=',sum,'\n')
					else:
						print("\n\nVous avez entrez un mauvais opérateur\n\n")
						pass
			except ValueError:
				print('\n\nPlease type an integer\n\n')
				pass
	#in case user type in no correct language, print it than start the program back
	else: 
		print('\n\nBad Language\n\n')
		main()
				
####calling main function####
main()
	