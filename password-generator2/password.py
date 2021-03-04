import random
'''
Allows us to take variables from the chars function
''' 

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&^&*'

# Choose the number of passwords that can be generated
number = input('Number of passwords? - ')
number = int(number)

# Choose the length of the password 
length = input ('Password length? - ')
length = int(length)

# for statement tells us that the characters that were entered above will make up the password
for p in range(number):
    password = ''
    for c in range(length):
        
        ''' 
        c stands for characters in this for statement
        '''

        password += random.choice(chars)
    print(password)