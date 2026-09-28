import time
import colorama

verity = True
counter = 0
init(autoreset=True)
while verity:
    print(Back.GREEN + "Hacking Pentagon in process...")
    time.sleep(0)  # Slows it down so you can see it printing
    
    counter += 1
    if counter >= 67:
        print("Access Granted!")
        verity = False  # This stops the loop
