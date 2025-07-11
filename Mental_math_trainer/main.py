#Mental math
#Addition of whole numbers only
import random
import time

#Settings
#set task (Addition or Subtraction or Multiplication or Division
#  or RANDOM or RANDOM Combination)
#set num_of_digits (1-digit values, 2-digit, 3-digit,
#  up to 7-digits or RANDOM Combination)
num_of_digits = 3
#set num_of_rows(3 - 10 total numbers)
num_of_rows = 3
#set timer (in seconds)
timer = 5

#Load Settings
num = (1,2,3,4,5,6,7,8,9,0)
try:
  #create Settings file
  print()
except FileExistsError:
  print()

def getRandomNum():
  return random.choice(num)

#task =

#num_of_digits = load it from Settings file

#num_of_rows = load from Settings file

#timer = load from Settings file


#Load Scores
try:
  #create Score file
  print()
except FileExistsError:
  print()

#Just stuff to make it more fun
def saveLastScore():
  print()

def getAvgOf10BestScores():
  print()

def saveLastTime():
  print()

def getAvgOf10BestTimes():
  print()


#Program starts here
while True:
  user_choice = input('''
             MAIN MENU
    Play(p) or change_Settings(s) or Quit(q)? ''')

  if user_choice.lower() == 'p':
    num_list = []
    add_list = []
    sum = 0
    ans = ''
    correctness = 0
    position = ''
    time_spent = 0

    print('Add')

    for j in range(num_of_rows): 
     for k in range(num_of_digits): 
        num_list.append(str(getRandomNum()))
     chunk = ''.join(num_list[j*num_of_digits : (j+1)*num_of_digits])
     add_list.append(chunk)

    for m in add_list:         #sum all the numbers
     print('    ',m)
     m = int(m)
     sum += m

    start_time = time.time() #Start counting how long the task takes the user

    print('🕑️ Timer.(Pls do NOT press any key now)')
    for j in reversed(range(1,(timer+1))):
      time.sleep(1)
      print(j)

    print('''    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalelalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala
    lalalalalalalalalalala''')
    print('\nEnter your answer:')
    print('          ---------------')
    
    ans = input('                ')
    print('          ---------------')

    end_time = time.time() #edit 

    time_spent = end_time - start_time
    if ans.isdigit():
      ans = int(ans)
      if ans == sum:
        print(ans,'is correct 🥳✅✅✅')
      else:
        print('WRONG❗❗')
        correctness = (ans/sum)*100
        if ans < sum:
          position = 'low-⌄'
        else:  #if ans > sum
          position = 'high-⌃'
        print('   correct answer was',sum,'\n')
        print(f' |you were『{correctness:.2f}%』close.\n |You guessed too {position}')
    else:
      print('Your answer MUST comprise entirely of whole numbers.')

    print(f'\n⏰ Time spent: {time_spent:.2f} seconds')

  elif user_choice.lower() == 's':
    #change_Settings
    print()

  elif user_choice.lower() == 'q':
    quit()

  else:
    print('\n  Sorry, wrong input.\n  Try pressing the letter "p" or "q".\n')