import random
colourlist=["RED","BLUE","GREEN","PINK","YELLOW","BLACK"]
attempt =5
won=0
lost=0

def startgame():
    return 
        
          
        
    
   
if _name_ == '_main_':
    print("Welcome to the color game:")
    name =str(input("please enter the name for score board:"))
    choice=int(input("Enter 1 to start the game \n2 to exit the game:"))  
    count =0
    
    if(choice==1):
        count+=1
        startgame()
        choice2=int(input("Enter 1 to see the scoreboard \n2 to play game \n3 to exit:"))
        if(choice2==1):
            print("Name:",name)
            print("you won:",won)
            print("you lost:",lost)
            print("Number of times game played",count)
            
        elif(choice2==2):
            count+=1
            startgame()
        elif(choice2==3):
            print("You Exit the game:")   
            
        attempt=5
    elif(choice==2):
        print("You Exit the game:")
