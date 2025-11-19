# code for simulated_bomb

import time
import timer_ascii_art

# add timer that calls this function every few seconds, can make this a list and access it using indexes where each index is shows ascii art of bomb ticking down
# can make a new file to only include bomb ascii art and timer- define it as a list and import it here


def bomb_status():
    print("Checking bomb status...")
    time.sleep(2)
    print(timer_ascii_art.bomb)
    print("Bomb is active.")
    time.sleep(2)
    print("Bomb will detonate in 10 seconds!")
    time.sleep(10)
    print(timer_ascii_art.explosion)
    print("BOOM! The bomb has detonated.")
    return 0

