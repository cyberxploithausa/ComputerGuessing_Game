import random

def computer_guess(x):
     low=1
     high=x
     feedback=' '
     while feedback != 'c':
          if high != low:
               guess = random.randint(low, high)
          else:
               guess = low
          feedback = input(f'Is {guess} too high(H), too low (L), correct (C): ').lower()
          if feedback == 'h':
               high = guess - 1
          elif feedback == 'l':
               low = guess + 1
                          
     print(f"Yay! the computer guessed your number, {guess} correctly!")
computer_guess(500)
         