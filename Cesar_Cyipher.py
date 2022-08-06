upper = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
lower = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
uchar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#ruchar = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
#rlchar = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
inverse_value = []
cipher = ''

text = input("Enter your message: ")
shiftval = int(input('Enter an encryption shift value (From 1 to 25)'))

# append all the caracter that nee to take their values from the switched list
for x in range(shiftval):
  inverse_value.append(lchar[-x - 1])

for char in text:    

    #Check for upper case 
    if char in uchar :
        try :
            uval = uchar.index(char) + shiftval
            cipher += uchar[uval]
        except IndexError :
            ind = uchar.index(char)
            r = 25 - int(ind)
            print(r)
            nv = int(shiftval) - int(r)
            print(nv)
            cipher += uchar[int(nv) - 1]

    #Check for lower case
    elif char in lchar : 
        try :
            lval = lchar.index(char) + shiftval
            cipher += lchar[lval]
        except IndexError :
            ind = lchar.index(char)
            r = 25 - int(ind)
            print(r)
            nv = int(shiftval) - int(r)
            print(nv)
            cipher += lchar[int(nv) - 1]

    #Add every other characters to de final string
    else : cipher += char

print(cipher)








