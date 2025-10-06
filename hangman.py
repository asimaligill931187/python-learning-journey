import  random
word_list=["aqib","apple","orange"]
chosen_word= random.choice(word_list)
print(chosen_word)

# 

Display=[]
for letter in chosen_word:
    Display+="_"
print(Display)
game_end=False
# user guess





while not game_end:
    
    user=input("please guess the letter?").lower()
    guess=user
    
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            Display[position]=letter
            print(Display)

    if "_" not in Display:
        game_end=True
        print("you Win")