#This is the file I use to test sections of code
import random

num =(0,1,2,3,4,5,6,7,8,9)
num_of_rows = 3
num_of_digits = 7
num_list = []
add_list = []
sum = 0

def getRandomNum():
    return random.choice(num)

for j in range(num_of_rows): #3
     for k in range(num_of_digits): #7
        num_list.append(str(getRandomNum()))
     chunk = ''.join(num_list[j*num_of_digits : (j+1)*num_of_digits])
     add_list.append(chunk)

for m in add_list:
    m = int(m)
    sum += m

print(sum)
    #how would you add groups of 3 strings (which are actually numbers) 
    # in a list together, where the 1st string(number) is 
    # the first digit of the new
    #number, the 2nd number, the 2nd digit etc. And you use this newly
    #formed 3-digit number to add to another 3 digit number
    # formed from the next sequence of numbers. Except
    #that you don't know how long the list is. All you know is that after
    #you gather a group of 3, the next that will follow is either
    #another group of 3 or the list will end.
# row1 = num_list[0:num_of_digits]
# row1 = ''.join(row1)
# row1 = int(row1)

# print(row1)
# print(type(row1))