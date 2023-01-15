import time
while True:
    CurrentLevel = int(input("What Level are you Currently on(0-5): "))
    if CurrentLevel > 5 or CurrentLevel < 0:
        print("Invalid Level")
    else:
        while True:
            GotoLevel = int(input("What Level do you want to go to (0-5): "))

            if CurrentLevel == GotoLevel:
                print("You are on the Same Level!")
            elif GotoLevel > 5 or GotoLevel < 0:
                print("Invalid Level")
            else:
                if GotoLevel > CurrentLevel:
                    NumberOfLoop = GotoLevel - CurrentLevel
                    for i in range(NumberOfLoop):
                        print("Level", CurrentLevel)
                        CurrentLevel = CurrentLevel + 1
                        time.sleep(0.25)
                else:
                    NumberOfLoop1 = CurrentLevel - GotoLevel
                    for i in range(NumberOfLoop1):
                        print("Level", CurrentLevel)
                        CurrentLevel = CurrentLevel - 1
                        time.sleep(0.25)
                print("Reached Level", CurrentLevel)