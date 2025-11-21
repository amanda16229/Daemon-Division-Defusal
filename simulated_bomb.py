# code for simulated_bomb

import time, threading
import timer_ascii_art

# add timer that calls this function every few seconds, can make this a list and access it using indexes where each index is shows ascii art of bomb ticking down
# can make a new file to only include bomb ascii art and timer- define it as a list and import it here


class BombTimer:
    def __init__(self):
        self.status = "inactive"
        self.defused = False
        self.time_remaining = 10
        self.running = False
    
    def start_countdown(self, callback=None):
        """Non-blocking countdown"""
        self.status = "active"
        self.running = True
        
        def countdown():
            print("Checking bomb status...")
            time.sleep(2)
            print(timer_ascii_art.bomb) 
            print("Bomb is active.")
            time.sleep(2)
            print(f"Bomb will detonate in {self.time_remaining} seconds!")
            
            while self.time_remaining > 0 and self.running and not self.defused:
                time.sleep(1)
                self.time_remaining -= 1
                if callback:
                    callback("timer_update", self.time_remaining)
            
            if self.defused:
                self.status = "defused"
                if callback:
                    callback("defused")
            else:
                print(timer_ascii_art.explosion)
                print("BOOM! The bomb has detonated.")
                self.status = "detonated"
                if callback:
                    callback("detonated")
        
        threading.Thread(target=countdown, daemon=True).start()
    
    def defuse(self):
        self.defused = True
        self.running = False

