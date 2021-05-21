import random
import os
import pygame
from pygame import mixer
from colorama import init, Fore, Back
init(autoreset=True)
pygame.init()

def turn(UnoDeck, Deck, pNames):
   win = False
   skip = False
   draw2 = False
   draw4 = False
   top_deck = draw_one_card(UnoDeck)
   
   while win == False:
      for x in Deck:
         if skip == True:
            print(pNames[Deck.index(x)]+" Your Turn Has Been Skipped :((")
            skip = False
            continue

         elif draw2 == True:

            for y in range(2):
               x.append(draw_one_card(UnoDeck))
            draw2 = False

         elif draw4 == True:
            for y in range(4):
               x.append(draw_one_card(UnoDeck))
            draw4 = False


         Play_card = take_input(top_deck,x,Deck.index(x), pNames)


         if Play_card == 'pass':
            x.append(draw_one_card(UnoDeck))
            continue

         elif Play_card[0] != 'Black':
            top_deck = Play_card
            x.remove(Play_card) 
            if Play_card[1] == 'Skip' or Play_card[1] == 'Reverse':
               skip = True
            elif Play_card[1] == 'Draw Two':
               draw2 = True

         elif Play_card[0] == 'Black':
            x.remove(Play_card)
            if Play_card[1] == 'Wild Draw Four':
               draw4 = True
            top_deck = (select_color(), '?')

         if len(x) == 0:
            print("Player ",pNames[Deck.index(x)]," Has Won !!\nCongrats :))")
            win = True
            break

         
def select_color():
   while 1 == 1:
      print("\nWILD CARD: \nSelect A Color:")
      print(Fore.RED+"1. Red")
      print(Fore.BLUE+"2. Blue")
      print(Fore.GREEN+"3. Green")
      print(Fore.YELLOW+"4. Yellow")
      temp = input("\nEnter You Card Within Valid Range: ")
      if temp.isnumeric():
         temp = int(temp)
         print(chr(27) + "[2J")
         if temp >=1 and temp <= 4:
            if temp == 1:
               return 'Red'
            elif temp == 2:
               return 'Blue'
            elif temp == 3:
               return 'Green'
            elif temp == 4:
               return 'Yellow'
   


def valid(top_deck, play_card):
   if top_deck[0] == play_card[0] or top_deck[1] == play_card[1]:
      return True
   elif play_card[0] == 'Black':
      return True
   return False

def take_input(top_deck, deck, player, pNames):
   while 1 == 1:
      # print(chr(27) + "[2J")
      # print(player+1)
      print(pNames[player],": It's your turn")

      print("Top Card: ",end="")
      if top_deck[0]=="Yellow":
         tmp = ""+str(top_deck)
         print("Top Card: "+Fore.YELLOW+tmp)
      elif top_deck[0]=="Red":
         tmp = ""+str(top_deck)
         print(Fore.RED+tmp)
      elif top_deck[0]=="Blue":
         tmp = ""+str(top_deck)
         print(Fore.BLUE+tmp)
      elif top_deck[0]=="Green":
         tmp = ""+str(top_deck)
         print(Fore.GREEN+tmp)
      else:
         tmp = "Top Card: "+str(top_deck)
         print(Back.WHITE+Fore.BLACK+tmp)     
      
      for x in range(len(deck)):
         if deck[x][0]=="Yellow":
            tmp = str(x)+": "+str(deck[x])
            print(Fore.YELLOW+tmp)
         elif deck[x][0]=="Red":
            tmp = str(x)+": "+str(deck[x])
            print(Fore.RED+tmp)
         elif deck[x][0]=="Blue":
            tmp = str(x)+": "+str(deck[x])
            print(Fore.BLUE+tmp)
         elif deck[x][0]=="Green":
            tmp = str(x)+": "+str(deck[x])
            print(Fore.GREEN+tmp)
         else:
            tmp = str(x)+": "+str(deck[x])
            print(Back.WHITE+Fore.BLACK+tmp)
         
         
      print ("\nEnter You Card Within Valid Range Or Type 'pass': ",end='')
      temp = input()
      print(chr(27) + "[2J")
      if temp == 'pass':
         return temp
      if temp.isnumeric():
         temp = int(temp)
         if temp>=0 and temp <= len(deck)-1:
            temp = int(temp)   
            if (valid(top_deck, deck[temp])) == True:
               return deck[temp]

def buildDeck():
   deck = []
   colors = ['Red','Green','Yellow','Blue']
   values = [0,1,2,3,4,5,6,7,8,9,'Draw Two','Skip','Reverse']
   wilds = ['Wild','Wild Draw Four']

   for x in colors:
      for y in values:
         cardval = (x,y)
         deck.append(cardval)
         deck.append(cardval)
   
   for i in range(4):
      deck.append(('Black',wilds[0]))
      deck.append(('Black',wilds[1]))

   return deck


def shuffleDeck(deck):
   for cardPos in range(len(deck)):
      randPos = random.randint(0,107)
      deck[cardPos],deck[randPos] = deck[randPos],deck[cardPos]
   return deck 


def draw_one_card(deck):
   return deck.pop()

def distribute_deck(game_deck):
   p1Cards=[]
   p2Cards=[]
   for i in range(7):
      p1Cards.append(game_deck.pop())
      p2Cards.append(game_deck.pop())
   return [p1Cards,p2Cards]

def welcomer():
   mixer.music.load("Good_Starts.mp3")
   mixer.music.play(-1)
   print(chr(27) + "[2J")
   print("Welcome To HU:UNO")
   playerNames=["",""]

   print("Enter 1st Player Name:")
   playerNames[0]=input() 
   print("Enter 2nd Player Name:")
   playerNames[1]=input()
   print(chr(27) + "[2J")
   return playerNames

unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)
disDeck = distribute_deck(unoDeck)
pNames = welcomer()

turn(unoDeck, disDeck ,pNames)