# -----------rock paper secissor----------
import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
images=[rock,paper,scissors]
choices=["Rock","Paper","Scissors"]

game_number=1
total_games_played=0
games_won_by_you=0
games_won_by_computer=0
games_drawn=0


# =====================welcome and start=============
print("\n")
print("🎮 🎮 Welcome to the ROCK, PAPER, SCISSOR Game!😊")

# ----------desire to play or not----------------
want_to_play=False
while not want_to_play:
  
    start_choice = input("Would you like to play? Type Y for 'Yes' and N for 'No':").lower()
    if start_choice=="y":
        want_to_play=True

        play_again =True

# ======================play again game loop======================
        while play_again:

            your_score=0
            computer_score=0
            draw_count=0
            current_round=1 
            game_history=[]
            total_games_played +=1

            print("\n" +"="*40)
            print(f"          🎮 Game {game_number}          ")
            print("="*40)

        



# -=====================round loop===================
            valid_round=False
            while not valid_round:

                try:
                    number_of_rounds=int(input("How many round you would like to play? \n"))

                    if  number_of_rounds<=0:
                        print("❌ Invalid number! Please enter a positive number.")
                    else:
                        valid_round=True
                except ValueError:
                    print("❌ Invalid input! Please enter a positive number.")
            
                
            while current_round<= number_of_rounds:
                print("\n" + "-" * 40)
                print(f"              ROUND {current_round}")
                print("-" * 40)  
     

# ============USER CHOICE====================
                valid_choice =False
                while not valid_choice:  
            
                    try:
                        user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper,2 for Scissors\n"))
                        if 0<=user_choice<=2:
                            valid_choice=True
                            print(f"\n👤 Your Choice:{choices[user_choice]}")
                            print(images[user_choice]) 
                        
                        else:
                            print("❌ Invalid choice! Please enter 0, 1, or 2.")
                    except ValueError:
                        print("❌ Invalid choice! Please enter 0, 1, or 2.")
                

            
# =================COMPUTER CHOICE==================
                computer_choice=random.randint(0,2)
                print(f"🤖 Computer Choice:{choices[computer_choice]}")
        
                print(images[computer_choice])


# =================DECISION COMPARSION===============
                if user_choice==computer_choice:
                    draw_count +=1
                    result="Game Draw"
                    print(f"Round {current_round}: {result}")
           
         
                elif (user_choice==0 and computer_choice==2) or (user_choice==1 and computer_choice==0) or (user_choice==2 and computer_choice==1):
                    result="You Win"
                    print(f"Round {current_round}: {result}")
                    your_score +=1
                
                else:
                    result="Computers Win"
                    print(f"Round {current_round}: {result}")
                    computer_score +=1
            
       

# -================ROUND SCORE=======================
                
                print("\n" + "-" * 40)
                print(f" SCORE  →  You: {your_score} | Computer: {computer_score} | Draws: {draw_count}")
                print("-" * 40)



                round_history=f"Round: {current_round :<3} Your Choice: {choices[user_choice]:<9}  Computer Choice={choices[computer_choice]:<9} →  {result} "
                game_history.append(round_history)
                current_round +=1

#=============ALL ROUNDS HISTORY IN ONE GAME================
            print("\n" + "=" * 40)
            print("              GAME HISTORY")
            print("-" * 40)
            for item in game_history:
                print(item)


# --------------score representation after one game----------------- 
            print("\n" + "=" * 40)
            print("              GAME SUMMARY")
            print("-" * 40)
            print(f"🎯 Rounds Played   : { number_of_rounds}")
            print(f"👤 Your Score      : {your_score}")
            print(f"🤖 Computer Score  : {computer_score}")
            print(f"🤝 Draws           : {draw_count}")
            print("=" * 40)

#-----------=----------final result after one game --------------
            print("\n")
            print("             🏆 FINAL RESULT")
            print("-" * 40)

            if your_score>computer_score:
                print(f"🎉 YOU WON!")
                print(f"You won {your_score} out of { number_of_rounds} rounds.")
                games_won_by_you +=1
        
            elif computer_score>your_score:
                print(f"🤖 COMPUTER WON!")
                print(f"Computer won {computer_score} out of { number_of_rounds} rounds.")
                games_won_by_computer +=1
            else:
                print("🤝 IT'S A DRAW!")
                print("Both players have the same score.")
                games_drawn +=1
            
            print("=" * 40)
  
#============PLAY AGAIN===================
            print("\n")

            valid_play_again=False
            while not valid_play_again:
                play_again_choice=input("Would You like to play again ? Type Y for 'Yes' and N for 'No': ").lower() 
                if play_again_choice=="y":  
                   game_number +=1  
                   valid_play_again=True
                elif play_again_choice=="n":
                   play_again=False
                   valid_play_again=True
                   print("\n")
                   print("😊 Thanks for playing!!!")
                        
                else:
                    print("❌ Invalid choice! Please Enter Y or N to Play Again")
                

    elif start_choice=="n":
        want_to_play=True
        print("😊 Thanks for visiting!!!")
        

    else:
        print("❌ Invalid choice! Please enter Y or N.")
   

# ==============overall statistics==================
print("\n" + "=" * 40)
print("             📊 OVERALL STATS")
print("-" * 40)
print(f"🎮 Game Played          : {total_games_played}")
print(f"👤 Game Won by you      : {games_won_by_you}")
print(f"🤖 Game Won by computer : {games_won_by_computer}")
print(f"🤝 Game Draw            : {games_drawn}") 
print("\n")
if total_games_played==0:
    print("📊 Win percentages: N/A (No games played)")
else:
    your_win_percentage= (games_won_by_you/total_games_played)*100
    computer_win_percentage =(games_won_by_computer/total_games_played)*100
    draw_percentage =(games_drawn/total_games_played)*100
    print(f"👤 Your Win %     : {your_win_percentage:.2f} ")
    print(f"🤖 Computer Win % : {computer_win_percentage:.2f} ")
    print(f"🤝 Draw  %        : {draw_percentage:.2f} ")

print("="*40)

