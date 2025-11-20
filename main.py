# main

import simulated_bomb, image_scanner, timer_ascii_art

import tkinter as tk

# run tkinter window in main, call other modules from here
# will need to import images to display in tkinter window
# have ascii cli art still in case tkinter doesnt work how we want

print("Main module running")

print(timer_ascii_art.logo)

simulated_bomb.bomb_status()


