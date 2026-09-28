import time
import colorama

verity = True
counter = 0
while verity:
    print("Hacking Pentagon in process...")
    time.sleep(0)  # Slows it down so you can see it printing
    
    counter += 1
    if counter >= 67:
        print("Access Granted!")
        verity = False  # This stops the loop
