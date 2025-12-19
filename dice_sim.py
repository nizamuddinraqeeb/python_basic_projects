import random
from tkinter import *

x = 'y'

# win = Tk()
# win.title("Dice Simulator")
# win.geometry("400x400")
# dice = Label(win, text="", font=("Helvetica", 100), fg="white", bg="green", width=2)
# dice.pack(expand=False, pady=30)
import tkinter as tk

root = tk.Tk()
root.title("Rounded Label Example")

canvas = tk.Canvas(root, width=200, height=200, highlightthickness=0, bg="#f0f0f0")
canvas.pack()

# Draw a rounded shape (circle)
circle = canvas.create_oval(20, 20, 180, 180, fill="#4CAF50", outline="")

# Add text in the middle
canvas.create_text(100, 100, text="Rounded Label", fill="white", font=("Helvetica", 12, "bold"))

root.mainloop()


# while x == 'y':#
#     num = random.randint(1, 6)
#     if num == 1:
#         print("[-----]")
#         print("[     ]")
#         print("[  *  ]")
#         print("[-----]")
#     elif num == 2:
#         print("[-----]")
#         print("[*    ]")
#         print("[    *]")
#         print("[-----]")
#     elif num == 3:
#         print("[-----]")
#         print("[*  * ]")
#         print("[  *  ]")
#         print("[-----]")
#     elif num == 4:
#         print("[-----]")
#         print("[*   *]")
#         print("[*   *]")
#         print("[-----]")
#     elif num == 5:
#         print("[-----]")
#         print("[* * *]")
#         print("[*  * ]")
#         print("[-----]")
#     elif num == 6:
#         print("[-----]")
#         print("[* * *]")
#         print("[* * *]")
#         print("[-----]")
        
#     def roll_again():
#         x = input("Roll the dice again? (y/n): ")
#         if x == 'n':
#             print("Thank you for playing!")
#             exit()
#         elif x == 'y':
#             print("Rolling the dice again...")
#         else:
#             print("Invalid input. Please enter 'y' or 'n'.")
#             roll_again()
#     roll_again()

#win.mainloop()