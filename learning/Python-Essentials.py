


#def mysplit(strng):
#    val = list(strng.split())
#   return val

#print(mysplit("To be or not to be, that is the question"))
#print(mysplit("To be or not to be,that is the question"))
#print(mysplit(" "))
#print(mysplit(" abc "))
#print(mysplit(""))

#t = 'theta'
#print(t.find('eta'))
#print(t.find('et'))
#print(t.find('the'))
#print(t.find('ha'))

#print('[' + 'Beta'.center(2) + ']')
#print('[' + 'Beta'.center(4) + ']')
#print('[' + 'Beta'.center(6) + ']')
#print('[' + 'Beta'.center(8) + ']')
#print('[' + 'Beta'.center(9) + ']')
#print('[' + 'Beta'.center(24) + ']')

#print("Alpha".capitalize())
#print('ALPHA'.capitalize())
#print(' Alpha'.capitalize())
#print('123'.capitalize())
#print("αβγδ".capitalize())

#for i in range(1,128) :
#    print(chr(i) , '-' , ord(chr(i)))

# Iterating through a string

#exampleString = 'silly walks'

#for ch in exampleString:
#    print(ch, end=' , ')

#print()

#def readint(prompt, min, max):
#    try :
#        val = int(input('Entrez le numéro a vérifier'))
#        if val < min or val > max : raise
#        else : return val
#    except ValueError :
#        print('Error: wrong input')
#    except RuntimeError : print('Error: the value is not within permitted range(',min,',',max,')')
    
#v = readint("Enter a number from -10 to 10: ", -10, 10)

#print("The number is:", v)

#school_class = {}
#while True:
#    name = input("Enter the student's name (or type exit to stop): ")
#    if name == 'exit':
#        break
    
#   score = int(input("Enter the student's score (0-10): "))
    
#    if name in school_class:
#        school_class[name] += (score,)
#    else:
#        school_class[name] = (score,)
        
#for name in sorted(school_class.keys()):
#    adding = 0
#    counter = 0
#    for score in school_class[name]:
#        adding += score
#        counter += 1
#    print(name, ":", adding / counter)

#exercice 4.1.3.7
#months = ['janvier','fevrier','mars','avril','mai','juin','juillet','aout','septembre','octobre','novembre','decembre']
#months_lenght = [31,28,31,30,31,30,31,30,31,30,31,30]
#def dayinmonth(yr,mnt):
#    month = mnt in months
#    leap = int(yr) % 4 
#    if int(yr) > 0 and int(yr) < 3000:
#        if month == False :
#            return None
#        else :
#            if leap == 0 :
#                leap = 29
#                print('Month : ' + str(mnt) + ' Of year : ' + str(yr) + ' Is : ' + str(leap)  + ' Days long !')
#            else :
#                print('Month : ' + str(mnt) + ' Of year : ' + str(yr) + ' Is : ' + str(months_lenght[months.index(mnt)]) + ' Days long !')        
#dayinmonth(input('Year : '),input('Month : '))


#exercice 3.1.6.9
#myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#temp_list = []
#for i in range(len(myList)) :
#   inlist = myList[i] in temp_list
#   if inlist == False :
#        temp_list.append(myList[i]) 
#temp_list.sort()
#print(temp_list)        
 

#exercice 3.1.2.15
#val = int(input('Type a number : '))
#steps = 0
#if val > 1 :
#    c0 = val
#    while c0 > 1 :
#        steps += 1
#        if (c0%2) == 0 :
#            c0 = c0 / 2
#            print(int(c0))
#        else :
#            c0 = 3*c0+1
#            print(int(c0))
#    print('Steps: ' + str(steps))        
#elif val == 1:
#    steps = 1
#    print(val)
#    print('Steps: ' + str(steps))
#else :
#    print('please type a positive number !')


#exercice 3.1.2.14
#print("The height of the pyramid:", height)
#blocks = int(input("Enter the number of blocks: "))
#blocks_left = blocks
#completeline = 0
#for i in range(blocks_left) :
#    if blocks_left <= i  :
#        print('Total completed line with ' + str(blocks) + ' Blocks = ' + str(completeline))
#        break
#    else:
#        blocks_left -= i + 1 
#        print('Block left : ' + str(blocks_left))
#        completeline += 1
#        print('Completed line(s) : ' + str(completeline))
    

#exercice simple for loop
#for c in range(1,6):
#    print(str(c) + ' Mississippi')
#print('Ready or not, here I come!')



#exercice while loop
#def main():
#    secret_number = 164
#    input_number = int(input('Please try to guest a the scecret number here : '))
#    count = 1
#    while input_number != secret_number :
#        if count == 1 : 
#            print('Ha ha! You\'re stuck in my loop!')
#            count += 1
#        else: main()
#    print('Congratulation, you found ' + str(secret_number) + ' , My screte number !!')
#main()


#exercice if elif else
#year = int(input('Enter the year to verify '))
#if year < 1582 :
#    print(str(year) + ' Is not within the gregorian calender period.')
#elif year % 4 != 0 :
#    print(str(year) + ' , it\'s a common year1')
#elif year % 100 != 0 :
#    print(str(year) + ' , it\'s a leap year1')
#elif year % 400 != 0 :
#    print(str(year) + ' , it\'s a common year2')
#else :
#    print('It\' a leap year2')


#exercise calcul de taxes
#income = float(input("Enter the annual income: "))
#if income <= 85528 :
#    tax = 0.18 * income -556.2
#else :
#    rate = (income - 85528) * 0.32
#    tax = 14839.2 + rate

#if tax <= 0 :
#    tax = 0.0
#tax = round(tax, 0)
#print("The tax is:", tax, "thalers")


#exercise if elif else
#answer_input = input('enter your text ')
#if answer_input == 'spathiphyllum':
#    print('No, I want a big Spathiphyllum!')
#elif answer_input == 'SPATHIPHYLLUM':
#    print('Yes - Spathiphyllum is the best plant ever!')
#else:
#    print('Spathiphyllum! Not ' + answer_input)


#excercice setter valeur booléan a la déclaration d'un variable
#n = int(input('type a number ')) >= 100 
#print(n)


#exercise  new line exit caracter
#print("\"I'm\"" + "\n" + "\"\"Learning\"\"" + "\n" + "\"\"\"Python\"\"\"")


#exercise fleche
#print('       * ' * 2 +'\n'+ '      * * ' * 2  +'\n'+''     *   * ' * 2 + '\n'+'    *     *' * 2+'\n'+'   *       *' * 2 + '\n' + '  *         *' + '\n' + " *           *" + '\n' + "****       ****" + '\n' + "   *       *" + '\n' + "   *       *"  + '\n' + "   *       *" + '\n' + "   *       *" + '\n' + "   *********")