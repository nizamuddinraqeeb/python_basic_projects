from tkinter import *
import random


app = Tk()

app.title("Rock Paper Scissors")
app.geometry("550x550")
app.configure(bg="#aff0c0")
app.resizable(False, False)


def reset_game():
    btn1["state"] = "active"
    btn2["state"] = "active"
    btn3["state"] = "active"
    l2.config(text="Your Choice")
    l3.config(text="Computer's choice")
    l4.config(text="result", bg="lightgrey")


def result_green(result):
    if result == "You Win!":
        l4.config(bg="green")
    elif result == "Computer Wins!":
        l4.config(bg="red")
    else:
        l4.config(bg="grey")


def disable_buttons():
    btn1["state"] = "disabled"
    btn2["state"] = "disabled"
    btn3["state"] = "disabled"


def choose_rock():
    computer_choice = random.choice(["🪨", "📄", "⚔️"])
    if computer_choice == "🪨":
        result = "It's a Draw!"
    elif computer_choice == "📄":
        result = "Computer Wins!"
    else:
        result = "You Win!"
    result_green(result)
    l2.config(text="You Chose: 🪨")
    l3.config(text=f"Computer chose: {computer_choice}")
    l4.config(text=result)
    disable_buttons()


def choose_paper():
    computer_choice = random.choice(["🪨", "📄", "⚔️"])
    if computer_choice == "📄":
        result = "It's a Draw!"
    elif computer_choice == "⚔️":
        result = "Computer Wins!"
    else:
        result = "You Win!"
    result_green(result)
    l2.config(text="You Chose: 📄")
    l3.config(text=f"Computer chose: {computer_choice}")
    l4.config(text=result)
    disable_buttons()


def choose_scissors():
    computer_choice = random.choice(["🪨", "📄", "⚔️"])
    if computer_choice == "⚔️":
        result = "It's a Draw!"
    elif computer_choice == "🪨":
        result = "Computer Wins!"
    else:
        result = "You Win!"
    result_green(result)
    l2.config(text="You Chose: ⚔️")
    l3.config(text=f"Computer chose: {computer_choice}")
    l4.config(text=result)
    disable_buttons()


# Labels
l1 = Label(app, text="Rock Paper Scissors", font=("cascadia code", 24, "bold"), relief='raised', padx=10, pady=10, fg="#a41208")
l1.pack(pady=20)

frame1 = Frame(app, bg="#aff0c0")
frame1.pack(pady=20)

l2 = Label(frame1, text="Your Choice", font=("lucida console", 11), relief='sunken',width=25, height=3)
l2.pack(side=LEFT)

l3 = Label(frame1, text="Computer's choice", font=("lucida console", 11), relief='sunken', width=25, height=3)
l3.pack(side=LEFT)

l4 = Label(app, text="Result", font=("lucida console", 11), relief='sunken', width=51, pady=10, bg="lightgrey")
l4.pack(pady=20)


# Buttons
frame2 = Frame(app, bg="#aff0c0")
frame2.pack(pady=20)

btn1 = Button(frame2, text="🪨", font=("arial", 40),command=choose_rock)
btn1.pack(side=LEFT, padx=5)
btn1.config(width=3, height=1)

btn2 = Button(frame2, text="📄", font=("arial", 40), command=choose_paper)
btn2.pack(side=LEFT, padx=5)
btn2.config(width=3, height=1)

btn3 = Button(frame2, text="⚔️",font=("arial", 40), command=choose_scissors)
btn3.pack(side=LEFT, padx=5)
btn3.config(width=3, height=1)

btn4 = Button(app, text="Reset", width=15, command=reset_game, bg="lightblue")
btn4.pack(pady=5)


#Credentials
l5 = Label(app, text="Developed by Nizamuddin Raqeeb", font=("cascadia code", 10), bg="#aff0c0")
l5.pack(side=BOTTOM, pady=5)


app.mainloop()
