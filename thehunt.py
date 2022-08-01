# Author: Melih Ateş
print("You have been riding your horse for a month by now and you see a little village a while away. hen you get to the village you stop, spend your last gold to buy some food for yourself and your horse. Then you hear the villager calling out to you.")
contract = input('Villager starts to tell you about the monster of the abandoned village and tells if you kill the monster, he will be pay back handsomely. Do you accept the deal? (z: yes/x: no)')
if contract == "z":  
    print("You mount your horse and start riding as you begin the journey.")
    
    magic = input("You arrive the abandoned village, wonder around a little. Then you hear a little weird noise in one of the houses. Inside one of the house you enter there is a very strong odor of a corpse. as you continue to walk, you hear meats shredding of a meat and a strong humming. You see a humanoid creature with scattered black fur on the visible red muscles, completely white eyes that gleam directly even in little bit of light. eating the remains of a corp. creature raises his head and sees you, you have the time to do only a magic trick. (z: fire/x: shield)")  
    if magic == "z":
        print("Monster escapes form fire magic by jumping to the wall then to you with great speed. Then cuts off your artery.")
        quit()
    if magic == "x":
        print("Monster jumps right at your throat. but with your magical shield, monster’s teeth broken.")
        
        sword = input("In pain monster falls down to the ground and gives you enough time to attack.  f(z: powerful attack/x: fast attack)")    
        if sword == "x":
            print("You take out your sword from it’s sheath then swing it the beast with great speed but it does little damage and makes beast more angry. Monster jumps at your arm and bites it, you drop your sword and become defenseless. Then monster rips off your arm and you fall to the ground in blood.")
            quit()
        if sword == "z":    
            print("You take out your sword from it’s sheath then you raise your sword.")
            
            escape = input("Monster sees this then raises its arm for protection. Your sword separates the arm from the body, monster tries to run while moaning. (z: wind magic/x: ice magic)")
            if escape == "z":
                print("Your wind magic does little affect, helps the monster to run faster and escape.")
                quit()
            if escape == "x":
                print("Ice magic slows down the monster, you run after the beast to the outside.")
            
                outside = input("Outside under the full moonlight, monster looks at you with all white glowing eyes and growling at you. Without one arm, monster struggling to upright, preparing itself to attack as you holding your sword tightly. Then monster starts to run at you. (z: swing your sword to upright/x: swing your sword to downright)")
                if outside == "z": 
                    print("Monster attacks from down. Grabbing your throat then sucks your whole blood.")
                    quit()
                if outside == "x": 
                    print("Monster attacks from down.")

                    reward = input("Your sword slashes his throat, the field turns into a bloodbath. (z: decapitate the monster)")
                    if reward == "z":
                        print("Monster on the ground, struggling, you end his pain with swing. You are tying his hand to your horse with rope, mounting your horse. Riding on the dusty road, under the full moon with the whispering of leaves of trees to get your prize.") 
                        quit()
                        
                
elif contract == "x":
    print("You mount your horse to settle another adventure.")
    quit()