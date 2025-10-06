print('''  
                  __..-----')
        ,.--._ .-'_..--...-'
       '-"'. _/_ /  ..--''""'-.
       _.--""...:._:(_ ..:"::. 
    .-' ..::--""_(##)#)"':. \ \)    \ _|_ /
   /_:-:'/  :__(##)##)    ): )   '-./'   '\.-'
   "  / |  :' :/""\///)  /:.'    --(       )--
     / :( :( :(   (#//)  "       .-'\.___./'-.
    / :/|\ :\_:\   \#//\            /  |  
    |:/ | ""--':\   (#//)              '
    \/  \ :|  \ :\  (#//)
         \:\   '.':. \#//
          ':|    "--'(#///)
                     (#///)
                     (#///)         ___/""\     
                      \#///\           oo##
                      (##///)         `-6 #
                      (##///)          ,'`.
                      (##///)         // `.
                      (##///)        ||o   //
                       \##///\        \-+--//
                       (###///)       :_|_(/
                       (sjw////)__...--:: :...__
                       (#/::'''             ""
                  '''           __;: :            "-._
          __..--""                  `---/ ;                '._
 ___..--""                             `-'                    "-..___
   (_ ""---....___                                     __...--"" _)
     """--...  ___"""""-----......._______......----"""     --"""
                   """"       ---.....   ___....----
 
   ''')

print("Welcome  to treasure island")
print("your mission to find treasure")
road=input("Your at crossedroad, where do you want to go? Type Left or Right?")
if road=='Right':
    print("Game over")
elif road=='Left':
    cross=input("Theirs island wait or swim?")
    if cross=="swim":
        print("Game over")
    elif cross=="wait":
        door=input("Which door? Type red yellow blue?")
        if door=="red":
            print("Game over")
        elif door=="blue":
            print("Game over")
        elif door=="yellow":
            print("Congrats you Win!")
            
else:
    print("Wrong choice:")
         