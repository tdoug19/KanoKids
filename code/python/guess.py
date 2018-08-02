#import random, easygui
import random

guess = 0
secret = random.randint(1,10)
tries = 0


#easygui.msgbox("def AHOY")

print ("Ahoy matey, I am Captian Blackbeard! "
        "guess my number between 1 and a 100 "
        "and I will give you my treasure.")
while guess != secret and tries < 3:
 #   //guess = easygui.integerbox("What's yer guess mater??")
    guess = float(input())
    
    if guess == secret: break
    
    if guess < secret:
        #easygui.msgbox("too low")
        print("Arrr your guess is too low!")
        
    else:
        print("Arr your guess is too high!")
        
    tries = tries + 1
        
if guess == secret:
    print("Nooooooo!!!  You get my treasure !!")
    
else:
    print("Hahaha.   My treasure is safe!!")
