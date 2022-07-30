# Surf Comp Game 
# Surf Comp Game 
# Scope:
# 1 player surfing game
# player is faced with decisions to match randomly generated conditions 
# descsion paints
# == choose competitor 
# == board choice /  random conditions
# == straight out or take the rip? / random set interval
# ==  wave choice /  random if a bigger one comes behind it 
# == shit talk  / could either help or harm deepening on random number 
# == 3 maneuver choices / each never has different risk level, based on random number out of 10, and different score
# == result 

from random import random


import random
from unicodedata import name
class Surfer:
    def __init__(self, name = "", board_size = 6, points = 0, wave = "", opponent = "", has_priority = True, time_since_set = random.randint(0, 5), heat_over = False, blackhead_choice_one = "", blackhead_choice_two = "", blackhead_choice_three = ""  ):
        self.name = name
        self.board_size = board_size
        self.points = points
        self.wave = wave
        self.opponent = opponent 
        self.has_priority = has_priority
        self.time_since_set = time_since_set
        self.heat_over = heat_over
        self.blackhead_choice_one = blackhead_choice_one
        self.blackhead_choice_two = blackhead_choice_two
        self.blackhead_choice_three = blackhead_choice_three
        
    def __repr__(self):
        return self.name
    def choose_opponent(self,opponent):
        if opponent == "1":
            kelly_slater = Surfer("Kelly Slater", 5.8, 0,"", player)
            print("Nice try, but surfing ain't that easy. You're opponent is Kelly Slater!")
            self.opponent = kelly_slater
        elif opponent == "2":
            liam_miller = Surfer("Liam Miller", 6.4, 0, "", player)
            print("Nice try, but you ain't that good. You're opponent is Liam Miller! ")
            self.opponent = liam_miller
        elif opponent == "3":
            duke_kahanamoku = Surfer("Duke Kahanamoku", 9.5, 0, "", player)
            print("Your opponent is the Duke! Get ready for a Hawaiian ass-whooping.")
            self.opponent = duke_kahanamoku
        else:print("You didn't enter one of the competitors numbers, so you didn't compete.")
    def choose_board(self,board):
        if board == "2":
            self.board_size = 6.7
            print(f"You chose the Al Merick1 Are you sure you can afford that, {self.name}?")
        if board == "1":
            self.board_size = 9
            print("You went with the log! The 1960s called, they want their board back.")
        if board == "3":
            self.board_size = 6.1
            print("You went with the shortboard! A high-performance shortboard does not a high-performance surfer make...")
    
    def choose_entry(self, entry):
        gets_out = random.randint(0, player.time_since_set)
        if entry == "1" and gets_out <= 1:
            print(f"{self.name} made it out back, that lucky duck! {self.opponent} is still on the beach!")
        elif entry == "1":
            print(f"Oh my.. A set just came as {self.name} was trying to get out and they got smashed. {self.opponent} took the rip and is waiting out back for their first wave!")
            self.has_priority = False
        elif entry == "2" and gets_out >= 1:
            print(f"{self.opponent} just got smashed up in the shorebreak while {self.name} floated lazily out the back. {self.name} has Priority!")
        else: 
            print(f"While {self.name} was waiting for the ocean's equivalent of a walking escalator, {self.opponent} punched straight out the back. {self.opponent}'s got priority!")
            self.has_priority = False
    def priority_call(self):
        if self.has_priority == True:
            self.points += 1
            print(f""".
    A {self.wave.size} meter set is coming and you have priority. Get ready to take off!
    """)
            if self.wave.name == "The Spit":
                self.player_at_spit()
                print("The second wave of the set is a bit smaller, but still solid!")
                self.opponent.opponent_at_spit()
            elif self.wave.name == "Blackhead":
                self.blackhead_action()
                self.opponent.blackhead_action()

        else: 
            self.opponent.points += 1
            print(f"""
    A {self.wave.size} meter set is coming and {self.opponent.name} has priority. Get ready for action!
    """) 
            if self.wave.name == "The Spit":
                player.opponent.opponent_at_spit()
                print("The second wave of the set is a bit smaller, but still solid!")
                player.player_at_spit()
            elif self.wave.name == "Blackhead":
                player.opponent.blackhead_action()
                self.blackhead_action()
        player.final_points()
    
    def player_at_spit(self):
        if self.board_size < 6.3:
            print("Your board doesn't have enough volume to get onto this monster. You have to paddle out towards the shoulder onto an open face.")
        else:
         self.the_spit_first_choice(input("""Your high-volume board got you into this monster nice and early. It looks like it's going to throw! Do you:            1. Bottom turn into the barrel!
            2. Go straight! """))
        self.the_spit_second_coice(input("""What maneuver will you try on this open face?
            1. Hang 10
            2. Layback Snap"""))    
    def opponent_at_spit(self):
        self.the_spit_first_choice(str(random.randint(1,2)))
        self.the_spit_second_coice(str(random.randint(1,2)))
    def the_spit_first_choice(self, spit_choice_one):
        if spit_choice_one == "2":
                print("{} rockets out in front of the detonating lip and mange to catch a reform with a bit of open face.".format(self.name))
                self.points += 3.0
        elif self.board_size > 8:
            self.heat_over = True
            print("{} tries to pull in with a hard bottom turn, but the single-fin can't hold the turn and the board slips out and gets smahsed by the lip, snapping it in half! Their heat is over.".format(self.name))        
        else: 
            print("{} does a tight bottom turn and locks into a high line through the tube. Life has never been so good for {}. They exit the barrel like a spit-take from God and fly onto an open face.".format(self.name,self.name))
            self.points += 7.0        
    def the_spit_second_coice(self, spit_choice_two):
        if self.board_size < 9:
            if spit_choice_two == "1":
                print("{}'s board isn't stable enough to walk the nose! They sink the nose and go down hard. They still got {} points for that wave.".format(self.name,self.points))
            elif spit_choice_two == "2":
                self.points += round(random.uniform(1.0, 2.0), 2)
                print("{} pumps down the open face, accelerates through a bottom turn, and finishes the wavee with a massive layback! {} point ride!".format(self.name, self.points))
        elif self.board_size > 8 and self.heat_over == False:
            if  spit_choice_two == "1":
                self.points += round(random.uniform(2.0, 4.0), 2)
                print("Way to bring back the classics, {}! They rode the nose all the way into the beach for a {} point ride.".format(self.name, self.points))
            if  spit_choice_two == "2":
                print("{} drives off the bottom to set up the layback and the single fin can't hold the turn! The board slides out and they go down on their face. It's a {} point ride.".format(self.name,self.points))
    def final_points(self):
        if self.points < self.opponent.points:
            print(f"The final score was {self.points} to {self.opponent.points}. {self.opponent.name} won the comp! Better luck next time.")
        else: print(f"The final score was {self.points} to {self.opponent.points}. You won the comp!")
    
    def blackhead_action(self):
        print(f"{self.name} takes off but the wave sections in front of them!")
        if self == player:
            self.blackhead_choice_one = input("""Do you 
        1. Pump and try to float over it?
        2. Go around in front of it?""")
            self.blackhead_action_one()
            if self.heat_over != True:
                self.blackhead_choice_two = input(f"""Now there is a {player.wave.size} meter high wall in front of you. Do you
            1. Throw some spray with a frontsid snap!
            2. Pump, then carve back to the pocket!""")
            self.blackhead_action_two()
            if self.heat_over != True:
                self.blackhead_choice_three = input("""Looks like this wave is about to close out on top of you. Do you
            1. Aim for the lip
            2. Aim for the flats""")
            
        else:
            self.blackhead_choice_one = str(random.randint(1,2))
            self.blackhead_action_one()
            self.blackhead_choice_two = str(random.randint(1,2))
            self.blackhead_action_two()
            self.blackhead_choice_three = str(random.randint(1,2))
        self.blackhead_action_three()

        
        
        


        
        
    def blackhead_action_one(self):
        if self.board_size > 8:
            if self.blackhead_choice_one == "1":
                self.heat_over = True
                print(f" {self.name} tries to float the section but their board is too big. They go down in the whitewater.")
            else: 
                self.points += round(random.uniform(1.5, 3.0), 2)
                print("They wield their voluminous board around the secion, barely keeping enough speed.")
        elif self.blackhead_choice_one == "1":
            self.points += round(random.uniform(3.0, 4.5), 2)
            print("They pump for speed and do a big float across the whitewater section!")
        else: 
            self.heat_over = True
            print("They try to dodge the section, but their board bogs on the flats and they go down in the whitewater.")    
    def blackhead_action_two(self):
        if self.heat_over != True:
            if self.blackhead_choice_two == "1":
                self.points += round(random.uniform(3.5, 5.0), 2)
                print(f"They accelerate through a bottom turn, then send a shower of spray with a tight snap at the top of the {player.wave.size} meter face.")
            else: 
                self.points += round(random.uniform(3.0, 4.5), 2)
                print(f"They acclerate out of the pocket and pull back around in a powerful carve.")
    def blackhead_action_three(self):
        if self.heat_over != True: 
            if self.blackhead_choice_three == "2":
                self.points += round(random.uniform(1.0,2.0), 2)
                print(f"{self.name} squeaks out in front of a closing section of whitewater and rides awy on their feet with a {self.points} point ride!")
            elif self.board_size < 6.3:  
                self.points += round(random.uniform(3.0, 4.0), 2)
                print(f"{self.name} does a big Air Reverse and lands in the whitewater. They ride away with a {self.points} point ride!")
                
            else:
                print(f"{self.name} goes airborne! The wind catches their board and they fall into the whitewater disgracefully.")
                    
            




player = Surfer()
class Wave: 
    def __init__(self, name = "", size = 2, speed = "", wind_offshore = True ):
        self.name = name
        self.size = size
        self.wind_offshore = wind_offshore
        self.speed = speed
        self.wind = "offshore" if self.wind_offshore == True else "onshore, goddammit"  
    def comp_announcement(self):
        print(f"Today's comp will be taking place at {self.name}. This is a {self.speed} {self.size} meter high wave, and the wind is {self.wind}. Choose your board accordingly!")
    def generate_wave():
        comp_wave = random.randint(1,2)
        if comp_wave == 1:
            the_spit = Wave("The Spit", 3, "speedy", True)
            player.wave = the_spit 
        elif comp_wave == 3:
            potato = Wave("Spud", 2, "fat", True )
            player.wave = potato
        elif comp_wave == 2:
            blackhead = Wave("Blackhead", 1.5, "speedy", False)
            player.wave = blackhead
        player.wave.comp_announcement()    
        


#Choose Opponent
print("Welcome to the Python Surf Competition! Get ready to pit your skills against the sickest of the sick!")
player.name = input("what's your name, grom? Type it and press Enter")
player.choose_opponent(input(""".
.
.
Okay, {player_name}, choose your opponent by typing their number and pressing Enter:
1. Liam Miller - difficulty level: Kook
2. Kelly Slater - difficulty level: GOAT
3. Duke Kahanamoku - difficulty level: OG""".format(player_name=player.name)))
#Display Conditions
proceed = input("""
This program chooses randomly from a set of options to decide where you'll be surfing. Aren't games realistic these days, {player_name}? Type ok to see where you're competing!""".format(player_name = player.name))
if proceed == "ok":
    Wave.generate_wave()
#Choose Board Based on Conditions
player.choose_board(input("""Pick from your quiver:
1. 9'0 Quarry Beach Longboard - single fin 
2. 6'7 Al Merick Happy Traveler - thruster
3. 6'1 JS Blackbox - twin fin
Type the number of your choice and press Enter!"""))
#Paddle out or TTake the rip?
player.choose_entry(input("""The bell rings and the clock is on! Do you paddle straight out or wait to find a rip? It's been {} minutes since the last set.
1. Go, go, go!
2. No way, scan for a rip.""".format(player.time_since_set)))

#Surf the wave
player.priority_call()


    
        
   

