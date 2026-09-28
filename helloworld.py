import time

verity = True
counter = 0

while verity:
    print("Hacking Pentagon in process...")
    time.sleep(0.5)  # Slows it down so you can see it printing
    
    counter += 1
    if counter >= 5:
        print("Access Granted!")
        verity = False  # This stops the loop
