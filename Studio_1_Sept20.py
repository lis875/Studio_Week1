
print("Welcome to story telling!")
print("We'll tell you a story, and every now and then there'll be twists and turns.")
print("You get to decide the twists and turns, we'll change the plot accordingly. ")
print("")
print("Let's begin with ")
print("With all the six stones, I could simply snap my fingers, and they would all cease to exist. I call that... mercy, Thanos exclaims ")
print("Thor throws his hammer at Thanos and it hits him in the chest \nThor says,'I told you, You'd die for that.' \nThanos screams in pain and then whispers,'you should've gone for the head' and Snaps his fingers")
print("Please choose what happens next: ")
snap_finger= input("1.The world ends \n2.Nothing happens ")
if (snap_finger== "The world ends") or (snap_finger=="1"):
    print("Everyone starts to disappear")
    print("Only few avengers are left and everyone else gets turned into dust")
    print("Years later, the avengers that were alive see Thanos using the stones again \nthey decide to trace Thanos and bring everyone back they lost.")
    print("They find Thanos")
    print("Steve asks Thanos, 'Where are they?'")
    print("Thanos responds, 'The universe required correction. After that, the stones served no purpose beyond temptation.'")
    print("Natasha asks: 'Where are the Stones?'")
    stones_input=input("Where do you want the stones to be: 1.Gone 2.Another twist")
    if (stones_input=="Gone") or (stones_input=="1"):
        print("Thanos responds wickedly, 'Gone. Reduced to atoms'")
    elif (stones_input=="Another twist") or (stones_input=="2"):
        print("The search for stones continues")

elif (snap_finger=="Nothing happens") or (snap_finger=="2"):
    print("Iron man tries to take the gaunlet from Thanos, but gets pushed away")
    print("Thanos says, 'I am inevitable' and snaps. Nothing happens. \nThanos discovers that the gauntlet no longer has the Infinity Stones, \nand that Stark used his armor's nano-technology to transfer the Stones to his arm")
    action_input=input("Would you want to see another snap: 1.Yes 2.No")
    if (action_input=="Yes") or (action_input=="1"):
        print("Tony Starks screams, 'And I... am... Iron Man!'")
        print("Stark snaps his fingers, and Thanos' army slowly fades into dust")
        print("Iron Man dies protecting everyone else")
    else:
        print ("The story gets boring if there's no snap, Maybe try with the snap")

else:
    print("That's incorrect option")
print("Thanks for reading the story, Hope you enjoyed!")





